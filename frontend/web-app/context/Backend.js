import { createContext } from "react";

export const BackendContext = createContext({
  backend: "http://localhost:8000",
});

export const BackendProvider = (props) => {
  return <BackendContext.Provider>{props.children}</BackendContext.Provider>;
};
