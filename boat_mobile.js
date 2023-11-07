const isSufficientFuel = (distance, literPerKm, fuelLeft) => {
    const requiredFuel = distance / literPerKm;
    if (fuelLeft >= requiredFuel) {
      return true;
    } else {
      return false;
    }
  };
  
  console.log(isSufficientFuel(300, 15, 20)); 
  console.log(isSufficientFuel(100, 10, 8));  
  