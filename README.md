# AI Mail Classifier｜AI 客服信件分類器

使用 **Python + uv + 本地 Ollama**，將客服信件分類為「訂單查詢、退款退貨、產品諮詢、技術支援、其他」，同時產生優先級、摘要與建議回覆。核心技術是 **LLM 結構化輸出（JSON Schema）**。

- **作品頁**：https://justtemp5678-sys.github.io/ai-mail-classifier/
- **原始碼**：https://github.com/justtemp5678-sys/ai-mail-classifier
- **自動部署**：`.github/workflows/pages.yml`（推送 main 後測試並部署 GitHub Pages）

## 本機執行

1. 安裝 [uv](https://docs.astral.sh/uv/) 與 [Ollama](https://ollama.com/)。
2. 在終端機執行 `ollama pull llama3.2`，確認 Ollama 正在執行（視系統需要執行 `ollama serve`）。
3. 下載本儲存庫後，在專案資料夾中執行：

```bash
uv run python main.py --text "您好，我上週訂的耳機還沒到，請幫我查詢物流進度。"
```

可選擇使用環境檔：複製 `.env.example` 為 `.env`，再執行 `uv run --env-file .env python main.py --text "我的商品想退貨"`。無需雲端 API Key。

## 測試

```bash
uv run python -m unittest discover -s tests -v
```

測試使用模擬的 Ollama HTTP 回應，**不是實際模型推論**。GitHub Actions 不需下載大型模型就能測試程式與發布靜態作品頁。

## 專案結構

- `main.py`：呼叫本地 Ollama `/api/chat` 並以 JSON Schema 限定回覆格式。
- `tests/test_main.py`：結構化輸出、錯誤回應與輸入驗證測試。
- `docs/`：GitHub Pages 作品展示（含互動式範例）。
- `.github/workflows/pages.yml`：CI 測試與 Pages 自動部署。
- `.env.example`：可自訂本地模型設定；真正的 `.env` 已由 `.gitignore` 排除。

## 執行結果與誠實揭露

作品頁顯示的是**人工設計的示意信件與預期分類結果，不是實際 LLM 執行截圖或實測結果**。本地安裝 Ollama 後可執行真正的模型推論。分類與回覆建議仍須人工確認，不應直接用於正式客服作業。

## AI 使用說明

使用 AI 協助規劃專案架構、撰寫 Python 程式、JSON Schema、測試與靜態作品頁。使用者應自行了解與驗證程式，並在本地執行 Ollama 後檢查真實輸出。**沒有將 API 金鑰或客戶個資提交到公開儲存庫**。

## 授權

教學展示專案，可自行改作與學習。
