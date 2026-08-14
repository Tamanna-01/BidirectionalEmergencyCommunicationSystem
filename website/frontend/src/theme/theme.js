import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    mode: "light",

    primary: {
      main: "#1565C0",
    },

    secondary: {
      main: "#42A5F5",
    },

    success: {
      main: "#2E7D32",
    },

    warning: {
      main: "#ED6C02",
    },

    error: {
      main: "#D32F2F",
    },

    background: {
      default: "#F5F7FA",
      paper: "#FFFFFF",
    },

    text: {
      primary: "#1F2937",
      secondary: "#6B7280",
    },

    divider: "#E5E7EB",
  },

  typography: {
    fontFamily: ["Poppins", "Roboto", "Helvetica", "Arial", "sans-serif"].join(
      ",",
    ),

    h4: {
      fontWeight: 700,
    },

    h5: {
      fontWeight: 600,
    },

    h6: {
      fontWeight: 600,
    },

    subtitle1: {
      fontWeight: 500,
    },

    body1: {
      fontWeight: 400,
    },

    button: {
      textTransform: "none",
      fontWeight: 600,
    },
  },

  shape: {
    borderRadius: 16,
  },

  components: {
    MuiPaper: {
      styleOverrides: {
        root: {
          borderRadius: 16,
          boxShadow: "0px 4px 12px rgba(0,0,0,0.08)",
        },
      },
    },

    MuiCard: {
      styleOverrides: {
        root: {
          borderRadius: 16,
          boxShadow: "0px 4px 12px rgba(0,0,0,0.08)",
        },
      },
    },

    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: 10,
          padding: "10px 22px",
          fontWeight: 600,
        },
      },
    },

    MuiAppBar: {
      styleOverrides: {
        root: {
          backgroundColor: "#FFFFFF",
          color: "#1F2937",
          boxShadow: "0px 2px 8px rgba(0,0,0,0.08)",
        },
      },
    },

    MuiDrawer: {
      styleOverrides: {
        paper: {
          backgroundColor: "#FFFFFF",
          borderRight: "1px solid #E5E7EB",
        },
      },
    },
  },
});

export default theme;
