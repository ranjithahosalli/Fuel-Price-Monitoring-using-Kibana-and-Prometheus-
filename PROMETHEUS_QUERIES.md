# Prometheus Queries & Visualization Guide

## 🔍 Prometheus Graph Queries

### **Basic Price Queries**

#### 1. All Fuel Prices
```
fuel_price
```
- **X-axis:** Time
- **Y-axis:** Price value
- **Visualization:** Multiple time series (one per city/fuel_type combination)

#### 2. Average Price Across All Cities
```
avg(fuel_price)
```
- **X-axis:** Time
- **Y-axis:** Average price
- **Visualization:** Single line chart

#### 3. Maximum Price by City
```
max by (city) (fuel_price)
```
- **X-axis:** Time
- **Y-axis:** Maximum price per city
- **Visualization:** Multiple lines (one per city)

#### 4. Average Price by City
```
avg by (city) (fuel_price)
```
- **X-axis:** Time
- **Y-axis:** Average price per city
- **Visualization:** Multiple lines

#### 5. Price for Specific City
```
fuel_price{city="mum"}
```
- **X-axis:** Time
- **Y-axis:** Price for Mumbai
- **Visualization:** Single line

#### 6. Price for Specific Fuel Type
```
fuel_price{fuel_type="Petrol"}
```
- **X-axis:** Time
- **Y-axis:** Petrol price across all cities
- **Visualization:** Multiple lines (one per city)

### **Price Update Metrics**

#### 7. Update Rate (Updates per Second)
```
rate(price_updates_total[5m])
```
- **X-axis:** Time
- **Y-axis:** Updates per second
- **Visualization:** Line chart showing update frequency

#### 8. Update Rate by City
```
sum by (city) (rate(price_updates_total[5m]))
```
- **X-axis:** Time
- **Y-axis:** Updates per second per city
- **Visualization:** Multiple lines (stacked or separate)

#### 9. Total Updates Over Time
```
increase(price_updates_total[1h])
```
- **X-axis:** Time
- **Y-axis:** Cumulative updates in last hour
- **Visualization:** Increasing line chart

#### 10. Total Updates by City
```
sum by (city) (increase(price_updates_total[1h]))
```
- **X-axis:** Time
- **Y-axis:** Total updates per city
- **Visualization:** Multiple lines or stacked area

### **Advanced Analytics**

#### 11. Price Volatility (Standard Deviation)
```
stddev_over_time(fuel_price[15m])
```
- **X-axis:** Time
- **Y-axis:** Standard deviation (volatility measure)
- **Visualization:** Line chart

#### 12. Price Change Rate (Derivative)
```
deriv(fuel_price[10m])
```
- **X-axis:** Time
- **Y-axis:** Price change rate (positive/negative)
- **Visualization:** Line chart with zero reference

#### 13. Price Deviation from Average
```
fuel_price - avg_over_time(fuel_price[15m])
```
- **X-axis:** Time
- **Y-axis:** Deviation from 15-minute average
- **Visualization:** Line chart (zero line reference)

#### 14. Rolling Average Price
```
avg_over_time(fuel_price[5m])
```
- **X-axis:** Time
- **Y-axis:** 5-minute rolling average
- **Visualization:** Smoothed line chart

#### 15. Maximum Price Over Window
```
max_over_time(fuel_price[15m])
```
- **X-axis:** Time
- **Y-axis:** Maximum price in 15-minute window
- **Visualization:** Line chart

#### 16. Minimum Price Over Window
```
min_over_time(fuel_price[15m])
```
- **X-axis:** Time
- **Y-axis:** Minimum price in 15-minute window
- **Visualization:** Line chart

### **Top/Bottom Queries**

#### 17. Top 5 Highest Prices
```
topk(5, fuel_price)
```
- **X-axis:** Time
- **Y-axis:** Top 5 price values
- **Visualization:** Top 5 lines

#### 18. Bottom 5 Lowest Prices
```
bottomk(5, fuel_price)
```
- **X-axis:** Time
- **Y-axis:** Bottom 5 price values
- **Visualization:** Bottom 5 lines

### **Filtered Queries**

#### 19. Multiple Cities (Regex)
```
fuel_price{city=~"mum|dlh|chn"}
```
- **X-axis:** Time
- **Y-axis:** Prices for Mumbai, Delhi, Chennai
- **Visualization:** Multiple lines

#### 20. Alert Threshold Check
```
fuel_price > 130
```
- **X-axis:** Time
- **Y-axis:** Boolean (1 or 0) - prices above ₹130
- **Visualization:** Step chart (0 or 1)

## 📊 Kibana Visualization Configuration

### **Data View: `fuel-price-events`**
- **Index Pattern:** `fuel-price-events*`
- **Timestamp Field:** `timestamp`

### **Visualization Types & Axis Configurations**

#### **1. Time Series - Average Price Over Time**
- **Type:** Line Chart / Area Chart
- **X-axis (Bottom):**
  - **Field:** `timestamp`
  - **Aggregation:** Date Histogram
  - **Interval:** 15 seconds / 1 minute
- **Y-axis (Left):**
  - **Field:** `price`
  - **Aggregation:** Average

#### **2. Price by City**
- **Type:** Line Chart
- **X-axis:**
  - **Field:** `timestamp`
  - **Aggregation:** Date Histogram
- **Y-axis:**
  - **Field:** `price`
  - **Aggregation:** Average
- **Split Series:**
  - **Field:** `city`
  - **Aggregation:** Terms
  - **Size:** 10

#### **3. Price by Fuel Type**
- **Type:** Area Chart (Stacked)
- **X-axis:**
  - **Field:** `timestamp`
  - **Aggregation:** Date Histogram
- **Y-axis:**
  - **Field:** `price`
  - **Aggregation:** Average
- **Split Series:**
  - **Field:** `fuel_type`
  - **Aggregation:** Terms

#### **4. Average Price by City (Bar Chart)**
- **Type:** Vertical Bar Chart
- **X-axis (Categories):**
  - **Field:** `city`
  - **Aggregation:** Terms
- **Y-axis (Values):**
  - **Field:** `price`
  - **Aggregation:** Average

#### **5. Price Heatmap (City vs Fuel Type)**
- **Type:** Heat Map
- **X-axis:**
  - **Field:** `city`
  - **Aggregation:** Terms
- **Y-axis:**
  - **Field:** `fuel_type`
  - **Aggregation:** Terms
- **Value:**
  - **Field:** `price`
  - **Aggregation:** Average

#### **6. Price Distribution**
- **Type:** Histogram
- **X-axis:**
  - **Field:** `price`
  - **Aggregation:** Histogram
  - **Interval:** 5.0 (₹5 buckets)
- **Y-axis:**
  - **Metric:** Count

#### **7. Top Cities by Average Price**
- **Type:** Pie Chart / Donut Chart
- **Slice:**
  - **Field:** `city`
  - **Aggregation:** Terms
  - **Size:** 5 (Top 5)
- **Metric:**
  - **Field:** `price`
  - **Aggregation:** Average

#### **8. Price Range (Min/Max)**
- **Type:** Vertical Bar Chart
- **X-axis:**
  - **Field:** `city`
  - **Aggregation:** Terms
- **Y-axis:**
  - **Field:** `price`
  - **Aggregations:**
    - Min (Add metric)
    - Max (Add metric)
- **Visualization:** Grouped bars

#### **9. Price Trend by Fuel Type and City**
- **Type:** Line Chart
- **X-axis:**
  - **Field:** `timestamp`
  - **Aggregation:** Date Histogram
- **Y-axis:**
  - **Field:** `price`
  - **Aggregation:** Average
- **Split Series:**
  - **Primary:** `city` (Terms)
  - **Secondary:** `fuel_type` (Terms)

#### **10. Price Statistics Dashboard Panel**
- **Type:** Metric
- **Metrics:**
  - Average price: `price` (Average)
  - Max price: `price` (Max)
  - Min price: `price` (Min)
  - Total events: Count

## 🎯 Quick Reference: Prometheus UI

1. **Go to:** http://localhost:9090
2. **Navigate to:** Graph tab
3. **Enter query** in the expression bar
4. **Click:** Execute
5. **View:** Graph tab (time series) or Console tab (current values)
6. **Adjust time range** using the time picker (top right)

## 🎯 Quick Reference: Kibana Visualization

1. **Go to:** http://localhost:5601
2. **Navigate to:** Visualize Library
3. **Click:** Create visualization → Lens
4. **Select data view:** `fuel-price-events`
5. **Configure axes** as per above configurations
6. **Save** and add to Dashboard

