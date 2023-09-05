import React from "react"
import { BrowserRouter as Router, Routes , Route , Link , redirect} from "react-router-dom"
import { Sample1 } from "./components/Sample1"
import { Sample2 } from "./components/Sample2"

export const App = () =>{
  return (
    <Router>
      <Routes>
        <Route path="frontend/" element={<h1>This is the main Page</h1>}></Route>
        <Route path="frontend/Sample1" element={<Sample1 />}></Route>
        <Route path="frontend/Sample2" element={<Sample2 />}></Route>
      </Routes>
    </Router>
  );
}
