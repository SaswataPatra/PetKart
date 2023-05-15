import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import './App.css';
import Home from './Home/home.component';
import PetList from './pets/pets-list.component';
import Checkout from './checkout/checkout.component';
import PetProfile from "./pets/pets-profile.component";
import Login from './auth/login.component';
import Register from './auth/register.component';
import authService from './auth/auth.service';

class App extends Component {
  constructor(props) {
    super(props);
    this.authService = new authService();
    this.state = {
      cart: []
    };
  }

  addToCart = (item) => {
    this.setState(prevState => ({
      cart: [...prevState.cart, item]
    }));
  }

  emptyCart = () => {
    this.setState({ cart: [] });
  }

  render() {
    return (
      <Router>
        <div>
          <div className="header">
            {/* Header content */}
          </div>
          <div className="container">
            <div className="head-top">
              {/* Logo */}
              {/* Menu */}
            </div>
          </div>
          <Route path='/home' component={Home} />
          <Route path='/pets' component={PetList} />
          <Route
            path='/single/:id'
            render={(props) => (
              <PetProfile {...props} addToCart={this.addToCart} />
            )}
          />
          <Route path='/checkout' component={Checkout} />
          <Route path='/auth/login' component={Login} />
          <Route path='/auth/register' component={Register} />
          {/* Additional routes */}
          <div className="footer w3layouts">
            {/* Footer content */}
          </div>
        </div>
      </Router>
    );
  }
}

export default App;
