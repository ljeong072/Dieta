const ChatMessage = ({ chat }) => {
  const getCleanText = (text) => {
  if (chat.role === "model") {
    // Extract text after "A:"
    const match = text.match(/A:\s*(.*)/s);
    const fullResponse = match ? match[1].trim() : text;

    // Find the last complete sentence that ends with ., !, or ?
    const lastSentenceMatch = fullResponse.match(/^(.*[.!?])[^.!?]*$/s);
    return lastSentenceMatch ? lastSentenceMatch[1].trim() : fullResponse;
  }
  return text;
};


  return (
    !chat.hideInChat && (
      <div className={`message ${chat.role === "model" ? "bot" : "user"}-message ${chat.isError ? "error" : ""}`}>
        <p className="message-text">{getCleanText(chat.text)}</p>
      </div>
    )
  );
};

export default ChatMessage;