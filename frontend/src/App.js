import { useState } from "react"
import ProgressBar from "./ProgressBar.component.js";
import logo from "./img/SipBudLogo.png"

// const testData = [
//   { bgcolor: "#6a1b9a", completed: 60 },
//   { bgcolor: "#00695c", completed: 30 },
//   { bgcolor: "#ef6c00", completed: 53 },
// ];

function App() {
  const [posts, setPosts] = useState([])

  const getPosts = async () => {
    try {
      console.log("Hello");
      const response = await fetch("http://localhost:3400/data")
      console.log("fetch done");
      // console.log(response)
      if (!response.ok) {
        throw Error(response.statusText)
      }
      const json = await response.json()
      setPosts(json)
      console.log(json)
    } catch (error) {
      console.error(error.message)
    }
    
  }

  return (
    <div className="container mx-auto p-4 m-4 border-solid border-2 border-gray-600 bg-gray-200">
      
      <h1 className="text-4xl text-gray-800 py-2 text-center">
        <img src={logo} width="300px"></img>
      </h1>
      <table className="table-auto py-4 border-gray-500">
      <ul>Daily Goal: {posts.intakeGoal}ml</ul>
      <div className="App">
      <ProgressBar key="bar" bgcolor={"#0081cc"} completed={posts.progress} />
      
      <ul>
      You are {posts.progress}% of the way to your daily goal!
      </ul>
      {/* {testData.map((item, idx) => (
        <ProgressBar key={idx} bgcolor={item.bgcolor} completed={item.completed} />
      ))} */}
          <ul className="flex flex-wrap py-4">
          <button
            type="button"
            className="bg-blue-500 hover:bg-blue-700 text-gray-800 font-bold m-1 py-2 px-4 rounded h-10"
            onClick={getPosts}
          >
            Refresh
          </button>
      </ul>
    </div>
      </table>
    </div>
    
  )
}

export default App