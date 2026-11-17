# Task 65 - Microsoft Azure AI Services (Weeks 10, 11, 12)

Study notes from the Microsoft Azure AI Services module (Weeks 11-12).
Service names have been rebranded over time (Cognitive Services -> Azure AI Services;
Form Recognizer -> Document Intelligence; LUIS -> Conversational Language Understanding),
so check the portal for current names.

## Week 11 - Plan, create, secure and deploy Azure AI Services
| Topic | Key points |
|---|---|
| Choosing a service | **Vision**: Computer Vision / Custom Vision / Face / Video Indexer. **Language**: Text Analytics, Translator, CLU, Question Answering. **Speech**: speech-to-text, text-to-speech, translation, speaker recognition. **Decision**: Anomaly Detector, Content Moderator, Personalizer. |
| Security | Manage keys (two keys, rotate regularly, store in **Azure Key Vault**); authenticate with key, **Microsoft Entra ID** token or managed identity; restrict network access with **Virtual Networks / private endpoints**. |
| Responsible AI | Six principles: fairness, reliability & safety, privacy & security, inclusiveness, transparency, accountability. |
| Create & manage | Create a resource in the Azure portal (single-service vs multi-service); configure **diagnostic logging**; monitor with Azure Monitor metrics and alerts; manage cost with pricing tiers (F0 free / S0 standard) and budgets. |
| Deploy | Find the endpoint + key in "Keys and Endpoint"; integrate into **CI/CD** (ARM/Bicep templates, GitHub Actions / Azure DevOps); use **prebuilt containers** (`docker run` with Eula, Billing, ApiKey parameters) for connected or edge environments. |
| Solutions | Anomaly Detector (time-series anomalies), Content Moderator (text/image moderation), Personalizer (reinforcement-learning recommendations), Metrics Advisor, Immersive Reader. |

## Week 11-12 - Vision and Video
- Image Analysis: tags, captions, object detection, OCR (Read API).
- Custom Vision: image classification and object detection trained on your own labelled images.
- Video: Video Indexer (transcripts, faces, topics) and spatial analysis.

## Week 12 - NLP, Knowledge Mining, Conversational AI
- **Text analysis**: sentiment, key phrases, entities, language detection, PII detection.
- **Speech**: speech-to-text, text-to-speech (SSML), speech translation.
- **Translator**: text and document translation.
- **Language understanding**: intents, utterances, entities -> build, train, test, publish.
- **Question answering**: knowledge base from FAQs/documents, multi-turn, chit-chat.
- **Knowledge mining (Azure AI Search)**: data source -> indexer -> skillset (OCR, key phrases) -> index -> query; knowledge store.
- **Conversational AI**: Azure Bot Service / Bot Framework, connect to channels (Teams, web chat), integrate CLU + question answering.

## Minimal Python example (Text Analytics) - run after creating a resource
```python
# pip install azure-ai-textanalytics
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

endpoint = "https://<your-resource>.cognitiveservices.azure.com/"
key = "<your-key>"          # never commit real keys; use environment variables
client = TextAnalyticsClient(endpoint, AzureKeyCredential(key))

docs = ["The NAVTTC AI course was excellent!", "The internet was slow and support was poor."]
for r in client.analyze_sentiment(docs):
    print(r.sentiment, r.confidence_scores)
```
