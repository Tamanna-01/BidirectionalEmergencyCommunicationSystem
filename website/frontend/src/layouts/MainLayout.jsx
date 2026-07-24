import { Box } from "@mui/material";
import { Outlet } from "react-router-dom";

import Sidebar from "../components/Sidebar/Sidebar";
import Topbar from "../components/Topbar/Topbar";

const SIDEBAR_WIDTH = 260;
const TOPBAR_HEIGHT = 70;

function MainLayout() {
  return (
    <Box sx={{ display: "flex", height: "100vh" }}>
      {/* Sidebar */}
      <Sidebar width={SIDEBAR_WIDTH} />

      {/* Right Side */}
      <Box
        sx={{
          flexGrow: 1,
          display: "flex",
          flexDirection: "column",
          ml: `${SIDEBAR_WIDTH}px`,
        }}
      >
        {/* Top Navigation */}
        <Topbar sidebarWidth={SIDEBAR_WIDTH} height={TOPBAR_HEIGHT} />

        {/* Page Content */}
        <Box
          component="main"
          sx={{
            flexGrow: 1,
            mt: `${TOPBAR_HEIGHT}px`,
            p: 3,
            overflowY: "auto",
            backgroundColor: "background.default",
          }}
        >
          <Outlet />
        </Box>
      </Box>
    </Box>
  );
}

export default MainLayout;
