# Fix "No Results Found" in Kibana

## ✅ Quick Fix Steps

### **Issue:** Kibana shows "No results found" even though data exists

### **Solution:**

1. **Extend Time Range (MOST COMMON FIX)**
   - Click the **time picker** (top right) showing "Last 15 minutes"
   - Change to: **"Last 24 hours"** or **"Last 7 days"**
   - Click **"Update"**
   
   **Why:** Your data might be older than 15 minutes, or you need to wait for new data.

2. **Verify Data View Configuration**
   - Go to: **Stack Management** → **Data Views**
   - Click on **"fuel-price-events"** data view
   - Ensure **Timestamp field** is set to: `timestamp`
   - Save if changed

3. **Check if Data View Exists**
   - If you see "No matching data stream..." error:
   - Go to: **Stack Management** → **Data Views** → **Create data view**
   - **Name:** `fuel-price-events`
   - **Index pattern:** `fuel-price-events*`
   - **Timestamp field:** `timestamp` (should be selectable)
   - Click **"Save"**

4. **Refresh Data in Kibana**
   - In Lens visualization, click the **refresh button** (circular arrow, top right)
   - Or manually refresh the browser page

5. **Verify Data Exists**
   - Go to: **Discover** (left menu)
   - Select data view: **fuel-price-events**
   - Set time range: **Last 24 hours**
   - You should see documents listed

---

## 🔍 Alternative: Check Data in Elasticsearch

**Verify data exists:**
```
http://localhost:9200/fuel-price-events/_count
```

**See sample document:**
```
http://localhost:9200/fuel-price-events/_search?size=1
```

**Check timestamp format:**
- Timestamps should be in ISO format: `2025-11-02T08:30:00Z`

---

## 🛠️ If Still No Results - Recreate Index

**Option 1: Delete and Restart App**
```powershell
# Delete index
Invoke-RestMethod -Method DELETE -Uri http://localhost:9200/fuel-price-events

# Restart app
cd fuel-monitoring
docker-compose restart app
```

**Option 2: Wait for New Data**
- The app creates new documents every ~15 seconds
- Wait 1-2 minutes after restart
- Then set time range to "Last 15 minutes" in Kibana

---

## ✅ Correct Visualization Configuration

Once data is visible, use these settings:

### **For Line Chart - Price Over Time:**
1. **X-Axis:** 
   - Drag `timestamp` field
   - Set to: **Date Histogram**
   - Interval: **Auto**
   
2. **Y-Axis:**
   - Drag `price` field  
   - Set to: **Average**
   
3. **Split by (optional):**
   - Drag `city` field
   - Set to: **Terms**

4. **Time Range:**
   - Set to: **Last 1 hour** or **Last 24 hours**

---

## 🎯 Step-by-Step: Fix Right Now

1. **Open Kibana:** http://localhost:5601
2. **Go to Discover:** Click "Discover" (left menu)
3. **Select data view:** `fuel-price-events`
4. **Change time:** Click time picker → Select **"Last 24 hours"**
5. **Verify:** You should see documents listed
6. **Go back to Lens:** Create new visualization
7. **Set time range:** **Last 24 hours** (important!)
8. **Create visualization:** Follow field configuration guide

---

## 💡 Pro Tip

**Always set a wider time range first** (Last 24 hours), then narrow down once you confirm data is visible.

If you see data in Discover but not in Lens:
- Refresh the Lens visualization
- Re-select the data view
- Check that X-axis uses `timestamp` with Date Histogram aggregation

