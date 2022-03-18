import { useContext } from "react";
import axios from "axios";
import { BackendContext } from "../context/Backend";

const GetBidProfiles = () => {
  // const backend = useContext(BackendContext);
  const link = "http://localhost:8000/bid/bid_profile";
  axios.get(link).then((response) => {
    console.log(response);
  });
};

export default GetBidProfiles;
