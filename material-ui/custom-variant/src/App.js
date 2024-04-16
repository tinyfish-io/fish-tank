import React from "react";
import ReactDOM from "react-dom";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import { Typography } from "@mui/material";

const theme = createTheme({
  typography: {
    // Define your custom variants here
    myCustomVariant: {
      fontFamily: "Arial, sans-serif",
      fontSize: "1.2rem",
      fontWeight: 400,
      lineHeight: 1.5,
    },
    anotherCustomVariant: {
      fontFamily: "Roboto, sans-serif",
      fontSize: "1rem",
      fontWeight: 500,
      lineHeight: 1.4,
    },
    // Add more custom variants as needed
  },
});

export default function App() {
  return (
    <ThemeProvider theme={theme}>
      <div>
        <Typography variant="myCustomVariant">Custom Variant Text</Typography>
        <p />

        <Typography variant="anotherCustomVariant">
          Another Custom Variant Text
        </Typography>
      </div>
    </ThemeProvider>
  );
}

// ReactDOM.render(<App />, document.getElementById("root"));
