import Head from "next/head";
import Footer from "./Footer";
import useStyles from "../utils/styles";

import Navbar from "./Navbar";

function Layout({ title, children }) {
  const classes = useStyles();
  return (
    <>
      <Head>
        <title>{title ? `${title} - Juvo` : "Juvo"}</title>
      </Head>
      <Navbar></Navbar>
      <main>{children}</main>
      {/* <Footer /> */}
    </>
  );
}

export default Layout;
