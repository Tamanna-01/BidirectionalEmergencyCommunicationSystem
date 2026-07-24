import { AppBar, Box, Toolbar, Typography } from "@mui/material";
import { useLocation } from "react-router-dom";

const pageTitles = {
  "/dashboard": "Dashboard",
  "/audio-detection": "Audio Detection",
  "/gesture-detection": "Gesture Detection",
};

function Topbar({ sidebarWidth, height }) {
  const location = useLocation();

  const title = pageTitles[location.pathname] || "EchoSafe";

  return (
    <AppBar
      position="fixed"
      elevation={0}
      sx={{
        width: `calc(100% - ${sidebarWidth}px)`,
        ml: `${sidebarWidth}px`,
        height,
        justifyContent: "center",
        borderBottom: "1px solid",
        borderColor: "divider",
        backgroundColor: "background.paper",
      }}
    >
      <Toolbar
        sx={{
          height: "100%",
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <Box>
          <Typography variant="h5" fontWeight={600}>
            {title}
          </Typography>

          <Typography variant="body2" color="text.secondary">
            AI Emergency Communication Platform
          </Typography>
        </Box>

        <Box
          sx={{
            display: "flex",
            alignItems: "center",
            gap: 1,
          }}
        >
          <Box
            sx={{
              width: 10,
              height: 10,
              borderRadius: "50%",
              bgcolor: "success.main",
            }}
          />

          <Typography variant="body2" color="text.secondary">
            System Ready
          </Typography>
        </Box>
      </Toolbar>
    </AppBar>
  );
}

export default Topbar;
