import { useEffect } from "react";
import { BackendProvider } from "../context/Backend";
import "../styles/globals.css";

function MyApp({ Component, pageProps }) {
  useEffect(() => {
    const jssStyles = document.querySelector("#jss-server-side");
    if (jssStyles) {
      jssStyles.parentElement.removeChild(jssStyles);
    }
  }, []);
  return (
    <BackendProvider>
      <Component {...pageProps} />
    </BackendProvider>
  );
}

export default MyApp;
