# reproduce Deep ANPR
Reproduce matthewearl's deep-anpr
https://github.com/matthewearl/deep-anpr

實作基於 tensorflow 和 CNN 的車牌辨識系統

使用說明:

* 至 SUN database (http://groups.csail.mit.edu/vision/SUN/) 下載檔案 SUN397.tar.gz 丟至跟 extractbgs.py 同一層目錄下
* 至 Dafont (http://www.dafont.com/uk-number-plate.font) 下載檔案 UKNumberPlate.ttf 丟同一層目錄下 fonts/ 資料夾下
* 將要用來測試模型的照片存成 in.jpg 丟至跟 detect.py 同一層目錄下
