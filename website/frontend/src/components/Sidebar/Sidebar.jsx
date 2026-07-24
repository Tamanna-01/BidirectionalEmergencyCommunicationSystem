import {
  Box,
  Divider,
  Drawer,
  List,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Typography,
} from "@mui/material";

import DashboardRoundedIcon from "@mui/icons-material/DashboardRounded";
import GraphicEqRoundedIcon from "@mui/icons-material/GraphicEqRounded";
import PanToolAltRoundedIcon from "@mui/icons-material/PanToolAltRounded";
import InfoRoundedIcon from "@mui/icons-material/InfoRounded";

import { NavLink } from "react-router-dom";

const menuItems = [
  {
    text: "Dashboard",
    path: "/dashboard",
    icon: <DashboardRoundedIcon />,
  },
  {
    text: "Audio Detection",
    path: "/audio-detection",
    icon: <GraphicEqRoundedIcon />,
  },
  {
    text: "Gesture Detection",
    path: "/gesture-detection",
    icon: <PanToolAltRoundedIcon />,
  },
];

function Sidebar({ width }) {
  return (
    <Drawer
      variant="permanent"
      sx={{
        width,
        flexShrink: 0,
        "& .MuiDrawer-paper": {
          width,
          boxSizing: "border-box",
          borderRight: "1px solid #E5E7EB",
        },
      }}
    >
      {/* Branding */}
      <Box
        sx={{
          py: 4,
          px: 3,
          textAlign: "center",
        }}
      >
        <Typography variant="h4" color="primary" fontWeight={700}>
          🛡 EchoSafe
        </Typography>

        <Typography variant="body2" color="text.secondary" sx={{ mt: 1 }}>
          AI Emergency Communication Platform
        </Typography>
      </Box>

      <Divider />

      {/* Navigation */}
      <List sx={{ mt: 2, px: 2 }}>
        {menuItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            style={{
              textDecoration: "none",
              color: "inherit",
            }}
          >
            {({ isActive }) => (
              <ListItemButton
                sx={{
                  mb: 1,
                  borderRadius: 2,
                  backgroundColor: isActive ? "primary.main" : "transparent",

                  color: isActive ? "white" : "text.primary",

                  "&:hover": {
                    backgroundColor: isActive ? "primary.dark" : "#EEF4FF",
                  },
                }}
              >
                <ListItemIcon
                  sx={{
                    color: isActive ? "white" : "primary.main",
                    minWidth: 40,
                  }}
                >
                  {item.icon}
                </ListItemIcon>

                <ListItemText primary={item.text} />
              </ListItemButton>
            )}
          </NavLink>
        ))}
      </List>
    </Drawer>
  );
}

export default Sidebar;
