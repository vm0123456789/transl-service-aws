// import "./App.css";
import React from "react";
import "./styles.css";

import Comment from "./components/Comment";

let data = [
  {
    name: "John",
    msg: "Hey, how are you doing?",
    ago: "2",
  },
  {
    name: "Giovanni",
    msg: "Ciao come stai",
    ago: "5",
  },
];

function App() {
  return (
    <div style={{ padding: 14 }} className="App">
      <h1>Comments</h1>
      {data.map((comment) => (
        <Comment comment={comment} />
      ))}
    </div>
  );
}

export default App;
