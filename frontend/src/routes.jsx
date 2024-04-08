import React from 'react'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Home from './Home'
import LoginPage from './LoginPage'
import Register from './Register'
import NotFound from './NotFound'
export default  function Router() {
    return (

        <BrowserRouter>
            <Routes>
                <Route path="/" exact Component={Home} cp />
                <Route exact Component={NotFound} />
                <Route path="/login" exact Component={LoginPage} />
                <Route path="/register" exact Component={Register} />
            </Routes>
        </BrowserRouter>

    )
}