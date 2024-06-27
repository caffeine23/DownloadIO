import React from "react";
import ReactDOM from "react-dom/client";
import App from "./pages/App.jsx";
import "./styles/index.css";
import { ChakraProvider } from "@chakra-ui/react";
import axios from "axios";

axios.defaults.baseURL = "http://localhost:3000";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <ChakraProvider>
      <App />
    </ChakraProvider>
  </React.StrictMode>
);
