# Kibana Visualization - X-Axis & Y-Axis Field Configuration

## 📊 Data View Information
- **Data View Name:** `fuel-price-events`
- **Index Pattern:** `fuel-price-events*`
- **Timestamp Field:** `timestamp`
- **Available Fields:**
  - `city` (keyword)
  - `fuel_type` (keyword)
  - `price` (number/float)
  - `timestamp` (date)

---

## 🎯 Visualization Type #1: Line Chart - Price Over Time

### **X-Axis (Horizontal)**
- **Field:** `timestamp`
- **Aggregation:** Date Histogram
- **Interval:** 
  - `Auto` (recommended)
  - OR `1 minute` (for detailed view)
  - OR `15 seconds` (for high-frequency updates)

### **Y-Axis (Vertical)**
- **Field:** `price`
- **Aggregation:** `Average`
- **Custom Label:** "Average Fuel Price (₹)"

### **Split Series (Optional - for Multiple Lines)**
- **Field:** `city`
- **Aggregation:** Terms
- **Order by:** Metric (Average of price)
- **Size:** 10
- **Custom Label:** "City"

**Result:** Multiple lines showing average price over time, one line per city

---

## 🎯 Visualization Type #2: Line Chart - Price by Fuel Type

### **X-Axis**
- **Field:** `timestamp`
- **Aggregation:** Date Histogram
- **Interval:** Auto or 1 minute

### **Y-Axis**
- **Field:** `price`
- **Aggregation:** `Average`
- **Custom Label:** "Average Price (₹)"

### **Split Series**
- **Field:** `fuel_type`
- **Aggregation:** Terms
- **Size:** 10

**Result:** Two lines - one for Petrol, one for Diesel

---

## 🎯 Visualization Type #3: Line Chart - Price by City AND Fuel Type

### **X-Axis**
- **Field:** `timestamp`
- **Aggregation:** Date Histogram
- **Interval:** Auto

### **Y-Axis**
- **Field:** `price`
- **Aggregation:** `Average`

### **Split Series (Multiple Levels)**
- **Primary Split:**
  - **Field:** `city`
  - **Aggregation:** Terms
- **Secondary Split:**
  - **Field:** `fuel_type`
  - **Aggregation:** Terms

**Result:** Multiple lines (e.g., Mumbai Petrol, Mumbai Diesel, Delhi Petrol, etc.)

---

## 🎯 Visualization Type #4: Vertical Bar Chart - Average Price by City

### **X-Axis (Categories)**
- **Field:** `city`
- **Aggregation:** Terms
- **Order by:** Metric (Average of price) - Descending
- **Size:** 10
- **Custom Label:** "City"

### **Y-Axis (Values)**
- **Field:** `price`
- **Aggregation:** `Average`
- **Custom Label:** "Average Price (₹)"

**Result:** Bar chart comparing average prices across cities

---

## 🎯 Visualization Type #5: Vertical Bar Chart - Price by Fuel Type

### **X-Axis**
- **Field:** `fuel_type`
- **Aggregation:** Terms
- **Size:** 10

### **Y-Axis**
- **Field:** `price`
- **Aggregation:** `Average`

**Result:** Two bars - one for Petrol average, one for Diesel average

---

## 🎯 Visualization Type #6: Grouped Bar Chart - Price by City AND Fuel Type

### **X-Axis**
- **Field:** `city`
- **Aggregation:** Terms
- **Size:** 10

### **Y-Axis**
- **Field:** `price`
- **Aggregation:** `Average`

### **Break Down By**
- **Field:** `fuel_type`
- **Aggregation:** Terms

**Result:** Grouped bars - each city has 2 bars (Petrol + Diesel side by side)

---

## 🎯 Visualization Type #7: Area Chart - Price Trend (Stacked)

### **X-Axis**
- **Field:** `timestamp`
- **Aggregation:** Date Histogram
- **Interval:** Auto

### **Y-Axis**
- **Field:** `price`
- **Aggregation:** `Average`

### **Split Series**
- **Field:** `city`
- **Aggregation:** Terms
- **Stacking:** Stacked area (enable in visualization settings)

**Result:** Stacked area chart showing price contribution by city over time

---

## 🎯 Visualization Type #8: Pie Chart - Price Distribution by City

### **Slice/Donut**
- **Field:** `city`
- **Aggregation:** Terms
- **Size:** 5 (Top 5 cities)

### **Metric (Size of Slice)**
- **Field:** `price`
- **Aggregation:** `Average`

**Result:** Pie chart showing which cities have highest average prices

---

## 🎯 Visualization Type #9: Heat Map - City vs Fuel Type

### **X-Axis**
- **Field:** `city`
- **Aggregation:** Terms
- **Size:** 10

### **Y-Axis**
- **Field:** `fuel_type`
- **Aggregation:** Terms

### **Color/Value**
- **Field:** `price`
- **Aggregation:** `Average`
- **Color Scale:** Gradient (low to high)

**Result:** Heat map - darker colors = higher prices

---

## 🎯 Visualization Type #10: Metric - Single Number Display

### **Metrics to Add:**
1. **Average Price**
   - **Field:** `price`
   - **Aggregation:** `Average`
   - **Label:** "Avg Fuel Price"

2. **Maximum Price**
   - **Field:** `price`
   - **Aggregation:** `Max`
   - **Label:** "Max Price"

3. **Minimum Price**
   - **Field:** `price`
   - **Aggregation:** `Min`
   - **Label:** "Min Price"

4. **Total Events**
   - **Aggregation:** `Count`
   - **Label:** "Total Updates"

**Result:** Dashboard panel with key statistics

---

## 🎯 Visualization Type #11: Histogram - Price Distribution

### **X-Axis**
- **Field:** `price`
- **Aggregation:** Histogram
- **Interval:** `5.0` (₹5 price buckets)
- **Custom Label:** "Price Range (₹)"

### **Y-Axis**
- **Metric:** Count
- **Custom Label:** "Number of Records"

**Result:** Histogram showing how many records fall in each price range

---

## 🎯 Visualization Type #12: Gauge/Progress - Price Level Indicator

### **Metric**
- **Field:** `price`
- **Aggregation:** `Average`

### **Gauge Settings:**
- **Min:** 90
- **Max:** 120
- **Target:** 110

**Result:** Gauge showing if average price is in acceptable range

---

## 📋 Step-by-Step: Creating Visualization in Kibana Lens

1. **Go to:** http://localhost:5601
2. **Navigate to:** Visualize Library (left menu)
3. **Click:** "Create visualization" → "Lens"
4. **Select Data View:** `fuel-price-events`
5. **Choose Visualization Type:** (Line, Bar, Area, etc.)

### **For X-Axis:**
- Drag `timestamp` field to "X-axis" section
- Set Aggregation: **Date Histogram**
- Set Interval: **Auto** or specific (1m, 15s)

### **For Y-Axis:**
- Drag `price` field to "Y-axis" section  
- Set Aggregation: **Average** (or Max, Min, Sum)
- Custom Label: Add descriptive name

### **For Split Series:**
- Drag `city` or `fuel_type` to "Color" or "Break down by" section
- Set Aggregation: **Terms**
- Set Size: 10 (to show all cities)

6. **Save** visualization
7. **Add to Dashboard**

---

## 🎨 Quick Reference Table

| Visualization Type | X-Axis Field | X-Aggregation | Y-Axis Field | Y-Aggregation | Split By |
|-------------------|--------------|---------------|--------------|---------------|----------|
| **Price Over Time** | `timestamp` | Date Histogram | `price` | Average | - |
| **Price by City** | `timestamp` | Date Histogram | `price` | Average | `city` (Terms) |
| **Price by Fuel Type** | `timestamp` | Date Histogram | `price` | Average | `fuel_type` (Terms) |
| **City Comparison** | `city` | Terms | `price` | Average | - |
| **Fuel Type Comparison** | `fuel_type` | Terms | `price` | Average | - |
| **Grouped Comparison** | `city` | Terms | `price` | Average | `fuel_type` (Terms) |
| **Heat Map** | `city` | Terms | `fuel_type` | Terms | Color: `price` (Avg) |
| **Pie Chart** | - | - | `price` | Average | `city` (Terms) |
| **Histogram** | `price` | Histogram (interval: 5) | - | Count | - |
| **Metric** | - | - | `price` | Average/Max/Min | - |

---

## 🔥 Top 3 Recommended Configurations

### **#1: Most Popular - Price Trend by City**
- **Type:** Line Chart
- **X-Axis:** `timestamp` (Date Histogram, Auto)
- **Y-Axis:** `price` (Average)
- **Split:** `city` (Terms)
- **Why:** Shows clear comparison between cities over time

### **#2: Simple Overview - Overall Average**
- **Type:** Line Chart or Area Chart
- **X-Axis:** `timestamp` (Date Histogram, 1 minute)
- **Y-Axis:** `price` (Average)
- **Split:** None
- **Why:** Clean, simple trend without clutter

### **#3: Comparison - Petrol vs Diesel**
- **Type:** Line Chart or Grouped Bar
- **X-Axis:** `timestamp` (Date Histogram) OR `fuel_type` (Terms)
- **Y-Axis:** `price` (Average)
- **Split:** `fuel_type` (Terms) OR `city` (Terms)
- **Why:** Clear fuel type comparison

---

## 💡 Pro Tips

1. **Always use `timestamp` for X-axis in time series** - This enables time-based filtering
2. **Use "Average" aggregation for price** - Gives meaningful trends
3. **Enable "Show values on chart"** - Makes numbers visible
4. **Set appropriate time range** - Use "Last 1 hour" or "Last 24 hours"
5. **Customize labels** - Make axes readable with descriptive names
6. **Use "Auto" interval first** - Kibana optimizes for your data density

---

## 🚀 Quick Copy-Paste Field Names

When creating visualizations, use these exact field names:

```
timestamp   (for X-axis - time series)
price       (for Y-axis - values)
city        (for splitting/grouping)
fuel_type   (for splitting/grouping)
```

Now you're ready to create beautiful visualizations in Kibana! 🎉

