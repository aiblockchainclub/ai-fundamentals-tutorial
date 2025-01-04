import React, { useState, useRef, useEffect } from "react";

const ChatMessage = ({
  message,
  isUser,
}: {
  message: string;
  isUser: boolean;
}) => (
  <div className={`flex ${isUser ? "justify-end" : "justify-start"} mb-4`}>
    <div
      className={`rounded-lg px-4 py-2 max-w-[80%] ${
        isUser
          ? "bg-blue-600 text-white rounded-br-none"
          : "bg-gray-700 text-gray-100 rounded-bl-none"
      }`}
    >
      {message}
    </div>
  </div>
);

export default function Chatbot() {
  const [messages, setMessages] = useState<
    Array<{ user: string; bot: string }>
  >([]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    setIsLoading(true);
    try {
      const response = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: input }),
      });
      const data = await response.json();
      setMessages([...messages, { user: input, bot: data.reply }]);
    } catch (error) {
      console.error("Error sending message:", error);
    } finally {
      setIsLoading(false);
      setInput("");
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="flex min-h-screen bg-gray-900 items-center justify-center p-4">
      <div className="w-full max-w-2xl h-[600px] flex flex-col bg-gray-800 rounded-lg shadow-xl">
        <div className="flex flex-col h-full p-4">
          <div className="mb-4 border-b border-gray-700 pb-4">
            <h2 className="text-2xl font-bold text-gray-100">Chat Assistant</h2>
            <p className="text-gray-400">How can I help you today?</p>
          </div>

          <div className="flex-grow mb-4 overflow-y-auto scrollbar-thin scrollbar-thumb-gray-600 scrollbar-track-gray-800">
            {messages.length === 0 ? (
              <div className="h-full flex items-center justify-center text-gray-500">
                Start a conversation...
              </div>
            ) : (
              <div className="space-y-4">
                {messages.map((msg, index) => (
                  <div key={index}>
                    <ChatMessage message={msg.user} isUser={true} />
                    <ChatMessage message={msg.bot} isUser={false} />
                  </div>
                ))}
                <div ref={messagesEndRef} />
              </div>
            )}
          </div>

          <div className="flex gap-2 border-t border-gray-700 pt-4">
            <input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Type your message..."
              className="flex-grow px-4 py-2 bg-gray-700 text-gray-100 rounded-lg 
                focus:outline-none focus:ring-2 focus:ring-blue-500 
                placeholder-gray-400 disabled:opacity-50"
              disabled={isLoading}
            />
            <button
              onClick={sendMessage}
              disabled={isLoading || !input.trim()}
              className="px-4 py-2 bg-blue-600 text-white rounded-lg 
                hover:bg-blue-700 focus:outline-none focus:ring-2 
                focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed
                transition-colors duration-200"
            >
              {isLoading ? (
                <svg className="animate-spin h-5 w-5" viewBox="0 0 24 24">
                  <circle
                    className="opacity-25"
                    cx="12"
                    cy="12"
                    r="10"
                    stroke="currentColor"
                    strokeWidth="4"
                    fill="none"
                  />
                  <path
                    className="opacity-75"
                    fill="currentColor"
                    d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"
                  />
                </svg>
              ) : (
                <svg
                  className="h-5 w-5"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"
                  />
                </svg>
              )}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
