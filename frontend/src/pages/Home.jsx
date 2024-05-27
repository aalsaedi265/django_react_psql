
import { useState, useEffect } from "react"
import api from "../api"

function Home() {
    
    const [notes, setNote] = useState([])
    const [content, setContent] = useState("")
    const [tittle, setTitle] = useState("")

    useEffect(() => {
        getNotes()
    },[])
    const getNotes = () => {
        api.get("/api/notes")
            .then((res) => res.data)
            .then((data) => {setNote(data); console.log(data)})
            .catch(err => alert(err))
    }

    const deleteNode = (id) => {
        api.delete(`/api/notes/delete/${id}/`)
            .then(res => {
                if (res.status == 204) alert("Note deleted!")
                else alert("Failed to delete note")
            }).catch(err => alert(err))
        getNotes()
    }

    const createNote = (e) => {
        e.preventDefault()
        api.post("/api/notes/", { content, tittle })
            .then(res => {
                if (res.status == 201) alert("note created")
                else alert("Failed to make note")
            }).catch(err => alert(err))
        getNotes()
    }


    return <div>
        <div>
            <h2>Notes</h2>
        </div>
        <h2>create a note</h2>
        <form></form>
    </div>
}

export default Home