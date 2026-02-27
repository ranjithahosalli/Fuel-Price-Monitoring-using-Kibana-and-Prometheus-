# How to Create Dashboard in Kibana

## 🎯 Step-by-Step Guide

### **Method 1: Create Dashboard from Scratch**

#### **Step 1: Create Visualizations First**

1. **Go to Kibana:**
   - Open: http://localhost:5601

2. **Create Your First Visualization:**
   - Click **"Visualize Library"** (left menu)
   - Click **"Create visualization"** button
   - Select **"Lens"** (recommended) or other visualization type

3. **Configure Visualization #1: Price Trend by City**
   - **Select Data View:** `fuel-price-events`
   - **Set Time Range:** Last 24 hours (top right)
   
   **For Line Chart:**
   - **X-Axis:** Drag `timestamp` → Set to **Date Histogram** (Auto interval)
   - **Y-Axis:** Drag `price` → Set to **Average**
   - **Split Series:** Drag `city` → Set to **Terms**
   
   - Click **"Save"** at top right
   - **Name:** "Price Trend by City"
   - **Save and return**

4. **Create Visualization #2: Petrol vs Diesel**
   - **Create visualization** → **Lens**
   - **Data View:** `fuel-price-events`
   - **X-Axis:** `timestamp` (Date Histogram)
   - **Y-Axis:** `price` (Average)
   - **Split Series:** `fuel_type` (Terms)
   - **Save as:** "Petrol vs Diesel Comparison"

5. **Create Visualization #3: City Comparison (Bar Chart)**
   - **Create visualization** → **Lens**
   - **Data View:** `fuel-price-events`
   - **X-Axis:** `city` (Terms)
   - **Y-Axis:** `price` (Average)
   - **Save as:** "Average Price by City"

6. **Create Visualization #4: Metric (Single Number)**
   - **Create visualization** → **Lens**
   - **Data View:** `fuel-price-events`
   - Drag `price` to workspace
   - Set aggregation to **Average**
   - **Save as:** "Average Fuel Price"

---

#### **Step 2: Create Dashboard**

1. **Go to Dashboards:**
   - Click **"Dashboards"** (left menu)
   - Click **"Create dashboard"** button

2. **Add Visualizations:**
   - Click **"Add panel"** or **"Add"** button
   - Select **"Add from library"**
   - You'll see all your saved visualizations
   - Click on each visualization to add it:
     - "Price Trend by City"
     - "Petrol vs Diesel Comparison"
     - "Average Price by City"
     - "Average Fuel Price"

3. **Arrange Panels:**
   - **Drag panels** to rearrange
   - **Resize panels** by dragging corners
   - **Organize layout:**
     - Top row: Metric (single number)
     - Second row: Two charts side by side
     - Bottom: Full-width line chart

4. **Save Dashboard:**
   - Click **"Save"** (top right)
   - **Name:** "Fuel Price Monitoring Dashboard"
   - **Description:** (optional)
   - Click **"Save"**

---

### **Method 2: Create Dashboard Directly**

1. **Go to Dashboards:**
   - http://localhost:5601/app/dashboards
   - Click **"Create dashboard"**

2. **Add Panel → Create New Visualization:**
   - Click **"Add panel"**
   - Select **"Create new"**
   - Choose **"Lens"**
   - Configure visualization (same as Method 1)
   - Click **"Save and return"** (adds to dashboard)

3. **Repeat for Multiple Panels:**
   - Add more panels with different visualizations
   - Each panel can show different data/visualizations

---

## 📊 Recommended Dashboard Layout

### **Layout 1: Monitoring Dashboard**

```
┌─────────────────────────────────────────┐
│  Metric: Avg Price | Max Price | Min   │
├─────────────────────────────────────────┤
│  Price Trend by City (Line Chart)      │
├───────────────────┬─────────────────────┤
│  Petrol vs Diesel │  City Comparison   │
│  (Line Chart)     │  (Bar Chart)        │
└───────────────────┴─────────────────────┘
```

### **Layout 2: Analytics Dashboard**

```
┌─────────────────────────────────────────┐
│  Price Trend by City (Full Width)      │
├───────────────────┬─────────────────────┤
│  Price by Fuel    │  Price Volatility   │
│  Type (Area)      │  (Line Chart)        │
├───────────────────┴─────────────────────┤
│  Heat Map: City vs Fuel Type            │
└─────────────────────────────────────────┘
```

---

## 🎨 Creating Each Visualization Type

### **1. Line Chart - Price Over Time**
- **X-Axis:** `timestamp` (Date Histogram, Auto)
- **Y-Axis:** `price` (Average)
- **Split by:** `city` (Terms)
- **Chart Type:** Line

### **2. Area Chart - Stacked**
- **X-Axis:** `timestamp` (Date Histogram)
- **Y-Axis:** `price` (Average)
- **Split by:** `city` (Terms)
- **Chart Type:** Area (Stacked)

### **3. Bar Chart - City Comparison**
- **X-Axis:** `city` (Terms)
- **Y-Axis:** `price` (Average)
- **Chart Type:** Vertical Bar

### **4. Metric - Single Number**
- **Field:** `price`
- **Aggregation:** Average
- **Chart Type:** Metric

### **5. Heat Map**
- **X-Axis:** `city` (Terms)
- **Y-Axis:** `fuel_type` (Terms)
- **Color:** `price` (Average)
- **Chart Type:** Heat Map

### **6. Pie Chart**
- **Slice:** `city` (Terms, Top 5)
- **Size:** `price` (Average)
- **Chart Type:** Pie or Donut

---

## 🔧 Dashboard Settings & Customization

### **Time Range:**
- **Set Global Time:** Click time picker (top right)
- **Per Panel:** Each panel can have its own time range
- **Recommended:** Last 24 hours or Last 1 hour

### **Refresh Settings:**
- **Auto Refresh:** Click refresh icon → Set interval (e.g., 30 seconds)
- **Manual Refresh:** Click refresh button

### **Panel Settings:**
- **Edit Panel:** Click panel → Edit (pencil icon)
- **Remove Panel:** Click panel → Remove
- **Duplicate Panel:** Click panel → Duplicate
- **Resize:** Drag panel corners

### **Dashboard Actions:**
- **Full Screen:** Click expand icon (top right)
- **Share:** Click share icon → Copy link
- **Export:** Click share → Export PDF/CSV

---

## 📋 Quick Reference: Dashboard Creation Steps

1. ✅ **Create Data View** (if not exists)
   - Stack Management → Data Views → Create
   - Name: `fuel-price-events`
   - Index: `fuel-price-events*`
   - Timestamp: `timestamp`

2. ✅ **Create Visualizations**
   - Visualize Library → Create → Lens
   - Configure X/Y axes
   - Save each visualization

3. ✅ **Create Dashboard**
   - Dashboards → Create dashboard
   - Add panels from library
   - Arrange and resize

4. ✅ **Save Dashboard**
   - Give it a name
   - Save

5. ✅ **View Dashboard**
   - Set time range
   - Auto-refresh (optional)
   - Share or export

---

## 🎯 Complete Example: Fuel Price Dashboard

### **Panel 1: Key Metrics (Top Row)**
- **Visualization:** Metric
- **Fields:** 
  - Average Price: `price` (Average)
  - Max Price: `price` (Max)
  - Min Price: `price` (Min)
- **Layout:** 3 metrics side by side

### **Panel 2: Price Trend (Main Chart)**
- **Visualization:** Line Chart
- **X-Axis:** `timestamp` (Date Histogram)
- **Y-Axis:** `price` (Average)
- **Split by:** `city` (Terms)
- **Layout:** Full width

### **Panel 3: Fuel Type Comparison**
- **Visualization:** Area Chart
- **X-Axis:** `timestamp` (Date Histogram)
- **Y-Axis:** `price` (Average)
- **Split by:** `fuel_type` (Terms)
- **Layout:** Left half

### **Panel 4: City Comparison**
- **Visualization:** Vertical Bar Chart
- **X-Axis:** `city` (Terms)
- **Y-Axis:** `price` (Average)
- **Layout:** Right half

---

## 💡 Pro Tips

1. **Start Simple:** Create 2-3 visualizations first, then add more
2. **Use Consistent Time Range:** Set global time for all panels
3. **Organize Layout:** Put most important chart at top
4. **Save Frequently:** Save each visualization before adding to dashboard
5. **Test Responsiveness:** Resize browser to see how dashboard adapts
6. **Use Auto Refresh:** For live monitoring (30s or 1m intervals)
7. **Name Clearly:** Use descriptive names for visualizations and dashboard

---

## 🚀 Quick Start Checklist

- [ ] Data view `fuel-price-events` exists
- [ ] Time range set to "Last 24 hours"
- [ ] Created at least 2 visualizations
- [ ] Created new dashboard
- [ ] Added visualizations as panels
- [ ] Arranged panels in desired layout
- [ ] Saved dashboard with descriptive name
- [ ] Set auto-refresh (optional)

---

## 🔗 Direct Links

- **Create Dashboard:** http://localhost:5601/app/dashboards/create
- **Visualize Library:** http://localhost:5601/app/visualize
- **Dashboards List:** http://localhost:5601/app/dashboards

---

Now you're ready to create beautiful, informative dashboards in Kibana! 🎉

