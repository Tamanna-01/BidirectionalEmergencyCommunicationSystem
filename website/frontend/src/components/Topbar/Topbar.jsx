import { AppBar, Box, Toolbar, Typography } from "@mui/material";
import { useLocation } from "react-router-dom";

const pageTitles = {
  "/dashboard": "Dashboard",
  "/audio-detection": "Audio Detection",
  "/gesture-detection": "Gesture Detection",
};

function Topbar({ height }) {
  const location = useLocation();
  const title = pageTitles[location.pathname] || "EchoSafe";

  return (
    /* Changed px: 3, pt: 3 to p: 3 to add equal padding on all sides, including the bottom */
    <Box sx={{ p: 3 }}> 
      <AppBar
        position="static"
        elevation={0}
        sx={{
          height,
          justifyContent: "center",
          backgroundColor: "#ffffff",
          border: "1px solid #e2e8f0",
          borderRadius: "18px", 
          color: "#1e293b",
          boxShadow: "0 4px 6px rgba(0, 0, 0, 0.02)",
        }}
      >
        <Toolbar
          sx={{
            height: "100%",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            px: { xs: 2, sm: 3 },
          }}
        >
          <Box>
            <Typography 
              variant="h5" 
              sx={{ 
                fontWeight: 700, 
                letterSpacing: "-0.01em",
                fontFamily: "system-ui, -apple-system, sans-serif"
              }}
            >
              {title}
            </Typography>

            <Typography 
              variant="body2" 
              sx={{ 
                color: "#6b7280",
                fontWeight: 500,
                mt: 0.25 
              }}
            >
              AI Emergency Communication Platform
            </Typography>
          </Box>

          <Box
            sx={{
              display: "flex",
              alignItems: "center",
              gap: 1.25,
              backgroundColor: "#f0fdf4",
              border: "1px solid #bbf7d0",
              padding: "6px 16px",
              borderRadius: "30px",
            }}
          >
            <Box
              sx={{
                width: 8,
                height: 8,
                borderRadius: "50%",
                bgcolor: "#16a34a",
                boxShadow: "0 0 8px rgba(22, 163, 74, 0.4)",
              }}
            />

            <Typography 
              variant="body2" 
              sx={{ 
                color: "#166534", 
                fontWeight: 600,
                fontSize: "0.85rem",
                textTransform: "uppercase",
                letterSpacing: "0.03em"
              }}
            >
              System Ready
            </Typography>
          </Box>
        </Toolbar>
      </AppBar>
    </Box>
  );
}

export default Topbar;