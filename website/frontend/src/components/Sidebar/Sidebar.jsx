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
          borderRight: "1px solid #e2e8f0", // Matches the light theme borders
          backgroundColor: "#ffffff",
        },
      }}
    >
      {/* Branding */}
      <Box
        sx={{
          py: 4,
          px: 3,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          textAlign: "center",
        }}
      >
        <Typography 
          variant="h5" 
          fontWeight={800} 
          sx={{ 
            color: "#1e293b", 
            letterSpacing: "-0.02em",
            display: "flex",
            alignItems: "center",
            gap: 1
          }}
        >
          <span style={{ color: "#3b82f6", fontSize: "1.2em" }}>🛡</span> EchoSafe
        </Typography>

        <Typography 
          variant="caption" 
          sx={{ 
            mt: 1.5, 
            color: "#6b7280",
            lineHeight: 1.6,
            fontWeight: 500
          }}
        >
          AI Emergency Communication Platform
        </Typography>
      </Box>

      <Divider sx={{ borderColor: "#f1f5f9", mb: 2, mx: 3 }} />

      {/* Navigation */}
      <List sx={{ px: 2, display: "flex", flexDirection: "column", gap: 0.5 }}>
        {menuItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            style={{
              textDecoration: "none",
              color: "inherit",
              display: "block"
            }}
          >
            {({ isActive }) => (
              <ListItemButton
                sx={{
                  borderRadius: "12px",
                  py: 1.25,
                  px: 2.5,
                  mb: 0.5,
                  backgroundColor: isActive ? "#3b82f6" : "transparent",
                  color: isActive ? "#ffffff" : "#475569",
                  transition: "all 0.2s ease",
                  boxShadow: isActive ? "0 4px 14px rgba(59, 130, 246, 0.4)" : "none",
                  
                  "&:hover": {
                    backgroundColor: isActive ? "#2563eb" : "#f8fafc",
                    transform: isActive ? "translateY(-2px)" : "none",
                  },
                }}
              >
                <ListItemIcon
                  sx={{
                    color: isActive ? "#ffffff" : "#64748b",
                    minWidth: 40,
                    transition: "color 0.2s ease",
                  }}
                >
                  {item.icon}
                </ListItemIcon>

                <ListItemText 
                  primary={item.text} 
                  primaryTypographyProps={{ 
                    fontWeight: isActive ? 700 : 500,
                    fontSize: "0.95rem",
                    fontFamily: 'system-ui, -apple-system, sans-serif'
                  }} 
                />
              </ListItemButton>
            )}
          </NavLink>
        ))}
      </List>
    </Drawer>
  );
}

export default Sidebar;