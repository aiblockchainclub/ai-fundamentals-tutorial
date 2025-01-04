import express from "express";
import bodyParser from "body-parser";
import cors from "cors";
import { GoogleGenerativeAI } from "@google/generative-ai";
const app = express();
app.use(bodyParser.json());
app.use(
  cors({
    origin: "*",
  })
);

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY || "");
const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

app.post("/chat", async (req, res) => {
  const { prompt } = req.body;
  const result = await model.generateContent(prompt);
  console.log(result.response.text());

  res.json({ reply: result.response.text() }).status(200);
});

app.listen(5000, () => console.log("Server running on port 5000"));
