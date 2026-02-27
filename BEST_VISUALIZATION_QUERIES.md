# Best Prometheus Queries for Clean Visualizations

## 🎯 Top Queries for Beautiful, Labeled Graphs

### **1. Fuel Price by City (Clean Multi-Line Graph)**
```
avg by (city, fuel_type) (fuel_price)
```
- **X-axis:** Time
- **Y-axis:** Average Price (₹)
- **Visualization:** Multiple clearly labeled lines (one per city/fuel_type combo)
- **Why it's clean:** Each series has distinct labels (e.g., `{city="mum", fuel_type="Petrol"}`)

### **2. Average Price Trend - All Cities Combined**
```
avg(fuel_price)
```
- **X-axis:** Time
- **Y-axis:** Average Price Across All Cities (₹)
- **Visualization:** Single smooth line
- **Why it's clean:** Shows overall trend without clutter
- **Label suggestion:** "Overall Average Fuel Price"

### **3. Price Comparison: City vs City**
```
fuel_price{city="mum"} or fuel_price{city="dlh"} or fuel_price{city="chn"}
```
- **X-axis:** Time
- **Y-axis:** Price (₹)
- **Visualization:** 3 clear lines comparing major cities
- **Why it's clean:** Direct comparison, easy to read

### **4. Petrol vs Diesel Price Trend**
```
avg by (fuel_type) (fuel_price)
```
- **X-axis:** Time
- **Y-axis:** Average Price (₹)
- **Visualization:** 2 lines (Petrol vs Diesel)
- **Why it's clean:** Simple, clear comparison
- **Label:** Lines auto-labeled as "Petrol" and "Diesel"

### **5. City-Wise Average Price (Bar Chart Style Query)**
```
max by (city) (fuel_price)
```
- **X-axis:** Time
- **Y-axis:** Maximum Price per City (₹)
- **Visualization:** Separate series per city
- **Why it's clean:** Each city has its own labeled line

### **6. Price Updates Frequency**
```
sum by (city) (rate(price_updates_total[5m]))
```
- **X-axis:** Time
- **Y-axis:** Updates per Second
- **Visualization:** Multiple lines showing update frequency per city
- **Why it's clean:** Shows activity level, clearly labeled by city

### **7. Price Volatility by City**
```
stddev_over_time(fuel_price[10m]) by (city)
```
- **X-axis:** Time
- **Y-axis:** Price Volatility (Standard Deviation)
- **Visualization:** Shows which cities have more price fluctuation
- **Why it's clean:** Easy to spot unstable markets

### **8. Smoothed Price Trend (5-Minute Rolling Average)**
```
avg_over_time(fuel_price[5m])
```
- **X-axis:** Time
- **Y-axis:** Smoothed Average Price (₹)
- **Visualization:** Smooth, less noisy line
- **Why it's clean:** Removes spikes, shows true trend

### **9. Price Range (Min-Max Shaded Area)**
Use these two queries together:
```
max_over_time(fuel_price[5m])
min_over_time(fuel_price[5m])
```
- **X-axis:** Time
- **Y-axis:** Price Range (₹)
- **Visualization:** Two lines showing price bounds
- **Why it's clean:** Visualizes price spread clearly

### **10. Top 3 Cities by Current Price**
```
topk(3, fuel_price)
```
- **X-axis:** Time
- **Y-axis:** Price (₹)
- **Visualization:** Only shows top 3 cities (cleanest view)
- **Why it's clean:** Focuses on highest prices, less clutter

### **11. Mumbai Petrol Price Trend**
```
fuel_price{city="mum", fuel_type="Petrol"}
```
- **X-axis:** Time
- **Y-axis:** Mumbai Petrol Price (₹)
- **Visualization:** Single focused line
- **Why it's clean:** Simplest possible visualization

### **12. Price Deviation from National Average**
```
fuel_price - avg(fuel_price)
```
- **X-axis:** Time
- **Y-axis:** Deviation from Average (₹)
- **Visualization:** Shows above/below average clearly
- **Why it's clean:** Zero line reference makes it intuitive
- **Note:** Positive = above avg, Negative = below avg

### **13. All Cities - Petrol Only**
```
fuel_price{fuel_type="Petrol"}
```
- **X-axis:** Time
- **Y-axis:** Petrol Price (₹)
- **Visualization:** Multiple lines, one per city (Petrol only)
- **Why it's clean:** Filters to one fuel type, reduces complexity

### **14. Price Change Rate (Speed of Change)**
```
deriv(fuel_price[5m])
```
- **X-axis:** Time
- **Y-axis:** Price Change Rate (₹/min)
- **Visualization:** Shows how fast prices are changing
- **Why it's clean:** Zero line shows increasing/decreasing trend

---

## 📊 Prometheus Graph Settings for Best Visualization

### **Recommended Graph Settings:**

1. **Graph Type:** 
   - Select "Graph" tab (not Console)
   
2. **Stacking:**
   - Off (for line charts)
   - On (for area charts if you want stacked)

3. **Y-axis Settings:**
   - Unit: None (or "currency" if supported)
   - Min: Auto
   - Max: Auto
   - Format: Default

4. **Legend:**
   - Show legend: ✅ Yes
   - Format: Table (shows all series clearly)

5. **Range Selection:**
   - Last 1 hour (for live data)
   - Last 6 hours (for trends)
   - Last 24 hours (for daily patterns)

---

## 🎨 Label Customization Tips

### **To see clearer labels in Prometheus:**

1. **Hover over legend** - Shows full label info
2. **Use `by (label)` clause** - Separates series clearly
3. **Use `label_replace()` for custom labels:**
   ```
   label_replace(
     fuel_price{city="mum"}, 
     "display_name", 
     "Mumbai Petrol", 
     "city", 
     ".*"
   )
   ```

---

## 🔥 Top 5 Recommended Queries for Presentations

### **#1: City Comparison (Most Popular)**
```
avg by (city) (fuel_price{fuel_type="Petrol"})
```
- Clean comparison of petrol prices across cities

### **#2: Overall Trend**
```
avg(fuel_price)
```
- Simple, professional trend line

### **#3: Petrol vs Diesel**
```
avg by (fuel_type) (fuel_price)
```
- Clear two-line comparison

### **#4: Activity Monitor**
```
sum(rate(price_updates_total[5m]))
```
- Shows system activity level

### **#5: Price Spread**
```
max_over_time(fuel_price[15m]) - min_over_time(fuel_price[15m])
```
- Shows price volatility (difference between high and low)

---

## 💡 Pro Tips for Clean Graphs

1. **Use `avg by ()` instead of individual series** - Reduces clutter
2. **Filter with `{}` selectors** - Focus on what you need
3. **Use `topk()` or `bottomk()`** - Show only relevant data
4. **Apply `_over_time()` functions** - Smooth noisy data
5. **Set appropriate time ranges** - 1h for live, 24h for trends
6. **Legend format: Table** - Easier to read than list

---

## 🚀 Quick Copy-Paste for Immediate Use

Copy these into Prometheus Graph tab at http://localhost:9090:

```
# Simple overall trend
avg(fuel_price)

# City comparison (Petrol)
avg by (city) (fuel_price{fuel_type="Petrol"})

# Petrol vs Diesel
avg by (fuel_type) (fuel_price)

# Top 3 cities
topk(3, fuel_price)

# Smoothed trend
avg_over_time(fuel_price[5m])
```

These will give you clean, labeled graphs immediately!

