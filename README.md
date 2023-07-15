這是一個使用 Google Maps API 的路線規劃程式，基於 Flask 框架開發。

如何運行
安裝所需套件：請確保已安裝下列套件

```text
pip install flask
pip install googlemaps
pyyaml
```

取得 Google Maps API 金鑰：在 Config.yml 檔案中設定 GoogleMap 的 API 金鑰

執行程式：在終端機中輸入以下指令以啟動伺服器

```text
python app.py
```

開啟瀏覽器：在瀏覽器中輸入 <http://localhost:5000/> 即可開啟應用程式

如何使用
在首頁輸入起點和終點地點，每行一個地點。

點擊「Submit」按鈕以獲取路線規劃結果。

系統將使用 Google Maps API 獲取每個起點和終點之間的路線、距離和預計時間。

結果將顯示在結果頁面，包括每個路線的起點和終點、路線地圖、距離和預計時間。

注意事項
請確保已在 Config.yml 檔案中設定了正確的 Google Maps API 金鑰。
程式在運行時需要網絡連接才能使用 Google Maps API。
requirements.txt:

```text
flask
googlemaps
pyyaml
```

將上述兩個檔案放置於你的程式碼相同的目錄中，並根據你的需求進行修改。README.md 檔案用於提供使用者對程式的說明和操作指南，requirements.txt 檔案則包含了程式所需的套件清單。
