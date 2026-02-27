# Prometheus Queries for Data Visualization

## 🎯 Copy-Paste Ready Queries for Prometheus Graph

### **1. Overall Average Price Trend (Single Line)**
```
avg(fuel_price)
```
- **Best for:** Simple trend overview
- **X-axis:** Time
- **Y-axis:** Average Price (₹)
- **Visualization:** Single smooth line showing overall market trend

---

### **2. Price by City (Multi-Line Comparison)**
```
avg by (city) (fuel_price)
```
- **Best for:** City comparison
- **X-axis:** Time
- **Y-axis:** Average Price per City (₹)
- **Visualization:** Multiple labeled lines (Mumbai, Delhi, Chennai, Bangalore)
- **Why it's clean:** Each city has its own clearly labeled line

---

### **3. Petrol vs Diesel Comparison**
```
avg by (fuel_type) (fuel_price)
```
- **Best for:** Fuel type comparison
- **X-axis:** Time
- **Y-axis:** Average Price (₹)
- **Visualization:** Two lines (Petrol and Diesel)
- **Why it's clean:** Simple, clear comparison

---

### **4. City-Wise Price (Petrol Only)**
```
avg by (city) (fuel_price{fuel_type="Petrol"})
```
- **Best for:** Comparing petrol prices across cities
- **X-axis:** Time
- **Y-axis:** Petrol Price per City (₹)
- **Visualization:** Multiple lines showing petrol prices

---

### **5. City-Wise Price (Diesel Only)**
```
avg by (city) (fuel_price{fuel_type="Diesel"})
```
- **Best for:** Comparing diesel prices across cities
- **X-axis:** Time
- **Y-axis:** Diesel Price per City (₹)
- **Visualization:** Multiple lines showing diesel prices

---

### **6. Specific City - All Fuel Types**
```
fuel_price{city="mum"}
```
- **Best for:** Focus on Mumbai prices
- **X-axis:** Time
- **Y-axis:** Mumbai Price (₹)
- **Visualization:** Multiple lines (Petrol and Diesel for Mumbai)

**Replace `mum` with:**
- `dlh` (Delhi)
- `chn` (Chennai)
- `bng` (Bangalore)

---

### **7. Top 3 Highest Prices**
```
topk(3, fuel_price)
```
- **Best for:** Focus on highest prices
- **X-axis:** Time
- **Y-axis:** Top 3 Price Values (₹)
- **Visualization:** Only shows 3 highest price series
- **Why it's clean:** Reduces clutter, focuses on outliers

---

### **8. Price Updates Rate (Activity Monitor)**
```
sum(rate(price_updates_total[5m]))
```
- **Best for:** System activity monitoring
- **X-axis:** Time
- **Y-axis:** Updates per Second
- **Visualization:** Single line showing update frequency

---

### **9. Price Updates by City**
```
sum by (city) (rate(price_updates_total[5m]))
```
- **Best for:** City-wise update frequency
- **X-axis:** Time
- **Y-axis:** Updates per Second per City
- **Visualization:** Multiple lines showing update activity

---

### **10. Smoothed Price Trend (5-Minute Rolling Average)**
```
avg_over_time(fuel_price[5m])
```
- **Best for:** Removing noise, showing true trend
- **X-axis:** Time
- **Y-axis:** Smoothed Average Price (₹)
- **Visualization:** Smooth, less noisy line
- **Why it's clean:** Removes spikes, shows trend clearly

---

### **11. Price Volatility (Standard Deviation)**
```
stddev_over_time(fuel_price[15m]) by (city)
```
- **Best for:** Measuring price stability
- **X-axis:** Time
- **Y-axis:** Price Volatility (Standard Deviation)
- **Visualization:** Shows which cities have more price fluctuation

---

### **12. Price Deviation from Average**
```
fuel_price - avg(fuel_price)
```
- **Best for:** Spotting above/below average prices
- **X-axis:** Time
- **Y-axis:** Deviation from Average (₹)
- **Visualization:** Zero line reference (positive = above avg, negative = below avg)
- **Why it's clean:** Easy to see which prices are above/below average

---

### **13. Price Range (Min-Max)**
```
max_over_time(fuel_price[5m])
min_over_time(fuel_price[5m])
```
- **Best for:** Visualizing price spread
- **X-axis:** Time
- **Y-axis:** Price Range (₹)
- **Visualization:** Two lines showing price bounds
- **How to use:** Run both queries, overlay them on same graph

---

### **14. Price Change Rate (Derivative)**
```
deriv(fuel_price[10m])
```
- **Best for:** Showing how fast prices are changing
- **X-axis:** Time
- **Y-axis:** Price Change Rate (₹/minute)
- **Visualization:** Positive = increasing, Negative = decreasing
- **Why it's clean:** Zero line makes trend clear

---

### **15. Multiple Cities Filter (Regex)**
```
fuel_price{city=~"mum|dlh|chn"}
```
- **Best for:** Comparing specific cities
- **X-axis:** Time
- **Y-axis:** Price (₹)
- **Visualization:** Lines for Mumbai, Delhi, Chennai only

---

### **16. Total Updates Cumulative**
```
sum(increase(price_updates_total[1h]))
```
- **Best for:** Total activity over time
- **X-axis:** Time
- **Y-axis:** Cumulative Updates
- **Visualization:** Increasing line showing total updates

---

### **17. Maximum Price by Fuel Type**
```
max by (fuel_type) (fuel_price)
```
- **Best for:** Highest prices comparison
- **X-axis:** Time
- **Y-axis:** Maximum Price (₹)
- **Visualization:** Two lines (Petrol max vs Diesel max)

---

### **18. Average Price by City and Fuel Type**
```
avg by (city, fuel_type) (fuel_price)
```
- **Best for:** Detailed breakdown
- **X-axis:** Time
- **Y-axis:** Average Price (₹)
- **Visualization:** Multiple lines (one per city/fuel combo)
- **Note:** Shows all combinations (Mumbai Petrol, Mumbai Diesel, Delhi Petrol, etc.)

---

### **19. Price Above Threshold (Alert Visualization)**
```
fuel_price > 130
```
- **Best for:** Alert threshold visualization
- **X-axis:** Time
- **Y-axis:** Boolean (1 = above threshold, 0 = below)
- **Visualization:** Step chart showing when prices exceed ₹130

---

### **20. Price Range Width (Max - Min)**
```
max_over_time(fuel_price[15m]) - min_over_time(fuel_price[15m])
```
- **Best for:** Price spread measurement
- **X-axis:** Time
- **Y-axis:** Price Range Width (₹)
- **Visualization:** Shows how much prices vary within 15-minute window

---

## 📊 Recommended Graph Settings in Prometheus

### **For Best Visualization:**

1. **Go to:** http://localhost:9090 → **Graph** tab

2. **Graph Settings:**
   - **Stacking:** Off (for line charts)
   - **Show exemplars:** Optional
   
3. **Legend:**
   - **Format:** Table (recommended - shows all series clearly)
   - **Show legend:** Yes

4. **Time Range:**
   - **Last 1 hour** (for live monitoring)
   - **Last 6 hours** (for trends)
   - **Last 24 hours** (for daily patterns)

5. **Y-Axis:**
   - **Unit:** None (or auto-detect)
   - **Format:** Default

---

## 🔥 Top 5 Recommended Queries for Presentations

### **#1: City Comparison (Most Popular)**
```
avg by (city) (fuel_price{fuel_type="Petrol"})
```
Copy this into Prometheus Graph for instant city comparison!

### **#2: Overall Trend**
```
avg(fuel_price)
```
Simple, professional trend line.

### **#3: Petrol vs Diesel**
```
avg by (fuel_type) (fuel_price)
```
Clear two-line comparison.

### **#4: Activity Monitor**
```
sum(rate(price_updates_total[5m]))
```
Shows system activity level.

### **#5: Smoothed Trend**
```
avg_over_time(fuel_price[5m])
```
Clean, noise-free visualization.

---

## 💡 Pro Tips

1. **Start with simple queries** - Use `avg()` or `avg by ()` first
2. **Use `by ()` clause** - Creates clean, labeled series
3. **Filter with `{}`** - Focus on specific cities/fuel types
4. **Use `topk()` or `bottomk()`** - Show only relevant data
5. **Apply `_over_time()` functions** - Smooth noisy data
6. **Set appropriate time ranges** - Wider ranges for trends, narrow for live data
7. **Legend format: Table** - Easier to read than list format

---

## 🚀 Quick Start

1. **Open:** http://localhost:9090
2. **Click:** Graph tab
3. **Paste any query** from above
4. **Click:** Execute
5. **View:** Beautiful graph with labels!

---

## 📋 Query Categories

### **Trend Analysis:**
- `avg(fuel_price)` - Overall trend
- `avg_over_time(fuel_price[5m])` - Smoothed trend
- `deriv(fuel_price[10m])` - Change rate

### **Comparison:**
- `avg by (city) (fuel_price)` - City comparison
- `avg by (fuel_type) (fuel_price)` - Fuel type comparison
- `topk(3, fuel_price)` - Top prices

### **Activity:**
- `rate(price_updates_total[5m])` - Update frequency
- `sum(increase(price_updates_total[1h]))` - Total updates

### **Analytics:**
- `stddev_over_time(fuel_price[15m])` - Volatility
- `fuel_price - avg(fuel_price)` - Deviation analysis
- `max_over_time(fuel_price[5m]) - min_over_time(fuel_price[5m])` - Range

---

All queries are ready to copy-paste into Prometheus Graph at http://localhost:9090! 🎉

