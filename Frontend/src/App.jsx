import CssBaseline from "@mui/material/CssBaseline";
import { Routes, Route, Navigate } from "react-router-dom";

import getRoutes from "./routes";

function App() {
	return (
		<>
			<CssBaseline />
			<Routes>
				{getRoutes()}
			</Routes>
		</>
	);
};

export default App;
