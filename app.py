from pathlib import Path
import json
import re
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Afficionado Coffee Roasters — Sales & Demand",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE = Path(__file__).parent
DATA_PATH = BASE / "data" / "Afficionado Coffee Roasters.xlsx"
STITCH_PATH = BASE / "assets" / "code.html"

@st.cache_data

def build_runtime_html(data_path: str, stitch_path: str) -> str:
    df = pd.read_excel(data_path)
    df["transaction_time"] = pd.to_datetime(
        df["transaction_time"].astype(str), format="%H:%M:%S", errors="coerce"
    )
    df = df.dropna(subset=["transaction_time", "store_location", "store_id"])
    df["hour"] = df["transaction_time"].dt.hour.astype(int)
    df["revenue"] = df["transaction_qty"] * df["unit_price"]

    # Stitch expects hourly store-level records. Use the real workbook values.
    agg = (
        df.groupby(["store_id", "store_location", "hour"], as_index=False)
        .agg(
            orders=("transaction_id", "count"),
            revenue=("revenue", "sum"),
            items=("transaction_qty", "sum"),
        )
        .sort_values(["store_id", "hour"])
    )

    records = []
    for r in agg.to_dict("records"):
        records.append({
            "hour": int(r["hour"]),
            "storeId": str(int(r["store_id"])),
            "storeName": str(r["store_location"]),
            "orders": int(r["orders"]),
            "revenue": round(float(r["revenue"]), 2),
            "items": int(r["items"]),
        })

    stores = []
    for r in (
        df[["store_id", "store_location"]]
        .drop_duplicates()
        .sort_values("store_id")
        .to_dict("records")
    ):
        stores.append({
            "id": str(int(r["store_id"])),
            "name": str(r["store_location"]),
            "code": f"Store #{int(r['store_id'])}",
        })

    html = Path(stitch_path).read_text(encoding="utf-8")

    # Replace the sample operational dataset with the actual Excel aggregation.
    dataset_js = "const rawOperationalDataset = " + json.dumps(records, separators=(",", ":")) + ";"
    html = re.sub(
        r"const rawOperationalDataset = \[.*?\];",
        dataset_js,
        html,
        count=1,
        flags=re.S,
    )

    stores_js = "const STORE_META = " + json.dumps(stores, separators=(",", ":")) + ";"
    html = html.replace("// Application State", stores_js + "\n\n  // Application State", 1)

    # Store dropdown and top navigation: use all real stores.
    store_options = '<option value="all">All Stores (Total Aggregation)</option>'
    for s in stores:
        store_options += f'<option value="{s["id"]}">{s["name"]} ({s["code"]})</option>'
    html = re.sub(
        r'<select([^>]*id="storeSelector"[^>]*)>.*?</select>',
        lambda m: '<select' + m.group(1) + '>' + store_options + '</select>',
        html,
        count=1,
        flags=re.S,
    )

    nav_buttons = ""
    for s in stores:
        nav_buttons += f'<button class="font-label-md text-label-md text-on-surface-variant hover:text-primary transition-colors pb-1 cursor-pointer top-nav-store" data-store="{s["id"]}">{s["name"]}</button>'
    html = re.sub(
        r'<div class="hidden md:flex items-center gap-5 ml-4 border-l border-outline-variant/40 pl-6" id="topStoreFilterNav">.*?</div>',
        '<div class="hidden md:flex items-center gap-5 ml-4 border-l border-outline-variant/40 pl-6" id="topStoreFilterNav">' + nav_buttons + '</div>',
        html,
        count=1,
        flags=re.S,
    )

    # The workbook has year + time, but no calendar date. Keep weekday control visible but disabled.
    html = html.replace(
        '<select class="w-full text-xs font-body-sm bg-surface-container-lowest border border-outline-variant/50 rounded-lg px-2.5 py-2 text-on-surface focus:outline-none focus:ring-1 focus:ring-secondary focus:border-secondary transition cursor-pointer appearance-none" id="dayOfWeekSelector">',
        '<select disabled title="Calendar date is not present in the source workbook" class="w-full text-xs font-body-sm bg-surface-container-lowest border border-outline-variant/50 rounded-lg px-2.5 py-2 text-on-surface focus:outline-none focus:ring-1 focus:ring-secondary focus:border-secondary transition cursor-not-allowed appearance-none opacity-60" id="dayOfWeekSelector">',
        1,
    )
    html = html.replace(
        "Timestamp format contains Time &amp; Year (2025); Day-of-Week activates automatically when calendar dates are supplied.",
        "Source workbook contains time + year only; calendar date is unavailable, so weekday analysis is disabled.",
    )

    # Match the actual workbook operating range: 6:00 AM–8:00 PM.
    html = html.replace('id="hourRangeInput" max="20" min="7" step="1" type="range" value="20"', 'id="hourRangeInput" max="20" min="6" step="1" type="range" value="20"')
    html = html.replace('7:00 AM – 8:00 PM', '6:00 AM – 8:00 PM')
    html = html.replace('<span class="">07:00</span>', '<span class="">06:00</span>')
    html = html.replace("(7–11)", "(6–11)")

    # Add a small runtime note to make the data provenance explicit.
    total_rows = len(df)
    html = html.replace(
        "Full Dataset Analytics • Dynamic Aggregation Engine",
        f"Full Dataset Analytics • {total_rows:,} transactions • Excel-backed aggregation",
        1,
    )

    # Replace store comparison block with a generic 3-store container.
    start_marker = '<!-- 3. Store Performance Comparison (5 cols) -->'
    end_marker = '<!-- 4. Store × Hour Heatmap with Multi-Metric Toggle (7 cols) -->'
    start = html.find(start_marker)
    end = html.find(end_marker)
    if start != -1 and end != -1:
        replacement = r'''<!-- 3. Store Performance Comparison (5 cols) -->
<div class="lg:col-span-5 bg-surface-container-lowest p-6 rounded-xl border border-outline-variant/30 shadow-[0_2px_8px_-2px_rgba(44,24,16,0.04)] flex flex-col justify-between">
<div>
<div class="flex items-center justify-between mb-4">
<div>
<h3 class="font-headline-sm text-headline-sm text-primary font-bold">Store Performance Comparison</h3>
<p class="font-body-sm text-body-sm text-on-surface-variant">Revenue, transactions and average ticket by location</p>
</div>
<span class="material-symbols-outlined text-outline">storefront</span>
</div>
<div class="space-y-3 mt-2" id="storeComparisonCards"></div>
<div class="grid grid-cols-2 gap-3 pt-4">
<div class="p-3 rounded-lg bg-surface border border-outline-variant/20 text-center">
<div class="text-[11px] font-label-sm text-outline uppercase font-semibold">Volume Leader</div>
<div class="font-headline-sm text-sm font-bold text-primary mt-0.5" id="storeLeaderTitle">—</div>
<div class="text-[11px] font-label-sm text-secondary font-medium" id="storeLeaderSub">—</div>
</div>
<div class="p-3 rounded-lg bg-surface border border-outline-variant/20 text-center">
<div class="text-[11px] font-label-sm text-outline uppercase font-semibold">Higher Basket Value</div>
<div class="font-headline-sm text-sm font-bold text-primary mt-0.5" id="storeAtvLeaderTitle">—</div>
<div class="text-[11px] font-label-sm text-secondary font-medium" id="storeAtvLeaderSub">—</div>
</div>
</div>
</div>
<div class="mt-4 pt-3 border-t border-outline-variant/30 text-xs text-on-surface-variant flex items-center justify-between">
<span>Active Revenue Share</span>
<span class="font-label-sm font-bold text-primary" id="storeRatioSummary">—</span>
</div>
</div>
'''
        html = html[:start] + replacement + html[end:]

    # Generic store comparison renderer.
    old_start = "    // 3. Store Performance Comparison Calculations"
    old_end = "    // 4. Store × Hour Heatmap Matrix Rendering"
    s = html.find(old_start)
    e = html.find(old_end)
    if s != -1 and e != -1:
        new_js = r'''    // 3. Store Performance Comparison Calculations
    const timeScoped = rawOperationalDataset.filter(d => {
      if (d.hour > state.maxHour) return false;
      if (state.selectedStore !== 'all' && d.storeId !== state.selectedStore) return false;
      if (state.daypart === 'morning' && (d.hour < 6 || d.hour > 11)) return false;
      if (state.daypart === 'afternoon' && (d.hour < 12 || d.hour > 16)) return false;
      if (state.daypart === 'evening' && (d.hour < 17 || d.hour > 20)) return false;
      return true;
    });

    const storeStats = STORE_META.map(store => {
      const rows = timeScoped.filter(d => d.storeId === store.id);
      const revenue = rows.reduce((a, d) => a + d.revenue, 0);
      const orders = rows.reduce((a, d) => a + d.orders, 0);
      const items = rows.reduce((a, d) => a + d.items, 0);
      return { ...store, revenue, orders, items, atv: orders ? revenue / orders : 0 };
    }).filter(s => state.selectedStore === 'all' || s.id === state.selectedStore);

    const totalStoreRevenue = storeStats.reduce((a, s) => a + s.revenue, 0);
    const cards = document.getElementById('storeComparisonCards');
    if (cards) {
      cards.innerHTML = storeStats.map((s, i) => {
        const share = totalStoreRevenue ? (s.revenue / totalStoreRevenue) * 100 : 0;
        const tone = i === 0 ? 'bg-primary-container' : (i === 1 ? 'bg-secondary' : 'bg-secondary-fixed');
        return `<div class="p-4 rounded-xl bg-surface-container-low border border-outline-variant/30">
          <div class="flex justify-between items-center mb-1.5">
            <div class="flex items-center gap-2"><span class="w-3 h-3 rounded-full ${tone}"></span><span class="font-headline-sm text-sm text-primary font-bold">${s.name} (${s.code})</span></div>
            <span class="font-label-md text-label-md text-secondary font-bold">${formatMoney(s.revenue)}</span>
          </div>
          <div class="w-full bg-surface-variant rounded-full h-2.5 overflow-hidden"><div class="${tone} h-full rounded-full" style="width:${share.toFixed(1)}%"></div></div>
          <div class="flex justify-between items-center mt-2 text-xs font-label-sm text-on-surface-variant">
            <span>${s.orders.toLocaleString()} orders (${share.toFixed(1)}% revenue share)</span><span class="font-semibold text-primary">Avg Ticket: ${formatMoney(s.atv)}</span>
          </div>
        </div>`;
      }).join('');
    }

    const volumeLeader = [...storeStats].sort((a,b) => b.orders-a.orders)[0];
    const atvLeader = [...storeStats].sort((a,b) => b.atv-a.atv)[0];
    if (volumeLeader) {
      const runner = [...storeStats].sort((a,b) => b.orders-a.orders)[1];
      const diff = runner && runner.orders ? Math.round(((volumeLeader.orders-runner.orders)/runner.orders)*100) : 0;
      document.getElementById('storeLeaderTitle').innerText = volumeLeader.name;
      document.getElementById('storeLeaderSub').innerText = runner ? `+${diff}% higher transactions vs ${runner.name}` : `${volumeLeader.orders.toLocaleString()} transactions`;
    }
    if (atvLeader) {
      document.getElementById('storeAtvLeaderTitle').innerText = atvLeader.name;
      document.getElementById('storeAtvLeaderSub').innerText = `${formatMoney(atvLeader.atv)} average ticket`;
    }
    document.getElementById('storeRatioSummary').innerText = storeStats.length ? storeStats.map(s => `${s.name}: ${totalStoreRevenue ? ((s.revenue/totalStoreRevenue)*100).toFixed(1) : '0.0'}%`).join(' • ') : 'No data';

    // 4. Store × Hour Heatmap Matrix Rendering
'''
        html = html[:s] + new_js + html[e+len(old_end):]

    # Replace heatmap store selection with STORE_META.
    html = re.sub(
        r"    // Stores to display based on store filter\n    const stores = \[\];.*?\n    // Determine value range",
        "    // Stores to display based on store filter\n    const stores = STORE_META.filter(s => state.selectedStore === 'all' || state.selectedStore === s.id);\n\n    // Determine value range",
        html,
        count=1,
        flags=re.S,
    )

    # Fix filter engine for all four dayparts and the real 6 AM start.
    html = re.sub(
        r"function getFilteredDataset\(\) \{.*?\n  \}",
        r'''function getFilteredDataset() {
    return rawOperationalDataset.filter(d => {
      if (state.selectedStore !== 'all' && d.storeId !== state.selectedStore) return false;
      if (d.hour > state.maxHour) return false;
      if (state.daypart === 'morning' && (d.hour < 6 || d.hour > 11)) return false;
      if (state.daypart === 'afternoon' && (d.hour < 12 || d.hour > 16)) return false;
      if (state.daypart === 'evening' && (d.hour < 17 || d.hour > 20)) return false;
      return true;
    });
  }''',
        html,
        count=1,
        flags=re.S,
    )

    # Fix the transaction-location text and the peak marker assumptions.
    html = html.replace("state.selectedStore === 'all' ? 'both locations' : (state.selectedStore === '5' ? 'Store #5' : 'Store #8')", "state.selectedStore === 'all' ? `${STORE_META.length} stores` : (STORE_META.find(s => s.id === state.selectedStore)?.code || state.selectedStore)")
    html = html.replace("const isPeak = h === 9;", "const isPeak = h === (getHourlyAggregates(data).length ? getHourlyAggregates(data).reduce((a,b) => b.orders > a.orders ? b : a).hour : -1);")
    html = html.replace("const peak9 = hourlyData.find(h => h.hour === 9);", "const peak9 = hourlyData.find(h => h.hour === peakHourItem.hour);")
    html = html.replace("const peak8 = hourlyData.find(h => h.hour === 8);", "const peak8 = hourlyData.find(h => h.hour === Math.max(6, peakHourItem.hour - 1));")
    html = html.replace("if (peak8 && peak9) {", "if (peak8 && peak9 && peak8.orders > 0) {")

    # Ensure reset returns to the actual 6 AM minimum.
    html = html.replace("hourInput.value = 20;", "hourInput.value = 20;")
    html = html.replace("state.maxHour = 20;", "state.maxHour = 20;")

    # Disable export placeholder if present and make it download the currently embedded data as CSV.
    export_js = r'''
    const exportBtn = document.getElementById('btnExportData');
    if (exportBtn) {
      exportBtn.addEventListener('click', () => {
        const rows = getFilteredDataset();
        const csv = ['hour,store_id,store_location,transactions,revenue,quantity', ...rows.map(r => `${r.hour},${r.storeId},"${r.storeName.replace(/"/g,'""')}",${r.orders},${r.revenue.toFixed(2)},${r.items}`)].join('\n');
        const blob = new Blob([csv], {type:'text/csv'});
        const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download='afficionado_filtered_hourly_data.csv'; a.click(); URL.revokeObjectURL(a.href);
      });
    }
'''
    html = html.replace("    // Initial render\n    renderDashboard();", export_js + "\n    // Initial render\n    renderDashboard();", 1)

    return html

html = build_runtime_html(str(DATA_PATH), str(STITCH_PATH))

# Streamlit is only the host; the visible dashboard is the Stitch UI itself.
# Streamlit is only the host; the visible dashboard is the Stitch UI itself.

st.markdown(
    """
    <style>
        body {
            margin: 0 !important;
        }

        .block-container {
            padding: 0 !important;
            max-width: none !important;
        }

        [data-testid="stAppViewContainer"] {
            background: #fbf9f5;
        }

        /* Hide Streamlit top header / black bar */
        [data-testid="stHeader"] {
            display: none !important;
        }

        /* Hide Streamlit toolbar */
        [data-testid="stToolbar"] {
            display: none !important;
        }

        iframe {
            border: 0 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(
    html,
    height=5000,
    scrolling=True
)
