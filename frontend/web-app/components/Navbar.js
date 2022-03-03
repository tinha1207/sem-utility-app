import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import IconButton from "@material-ui/core/IconButton";
import MenuIcon from "@material-ui/icons/Menu";
import Menu from "@material-ui/icons/Menu";
import { MenuList } from "@material-ui/core";
import { MenuItem } from "@material-ui/core";
import { Drawer } from "@material-ui/core";

import Link from "next/link";

export const Navbar = () => {
  const navList = [
    { "Keyword App": { link: "/utilities/Keyword", name: "Keyword App" } },
  ];

  return (
    <AppBar position="static">
      <Toolbar variant="dense">
        <IconButton edge="start">
          <MenuIcon />
        </IconButton>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
