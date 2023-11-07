const student1 = {
    name: "Jordan",
    age: 19,
    grades: [90, 85, 88, 92, 76],
    calculateAverage: function() {
      const sum = this.grades.reduce((total, grade) => total + grade, 0);
      return sum / this.grades.length;
    }
  };
  
  const student2 = {
    name: "Gilad",
    age: 22,
    grades: [100, 34, 56, 87, 20],
    calculateAverage: function() {
      const sum = this.grades.reduce((total, grade) => total + grade, 0);
      return sum / this.grades.length;
    }
  };
  
  const student3 = {
    name: "Matan",
    age: 62,
    grades: [70, 40, 32, 100, 95],
    calculateAverage: function() {
      const sum = this.grades.reduce((total, grade) => total + grade, 0);
      return sum / this.grades.length;
    }
  };
  
  const student4 = {
    name: "Koral",
    age: 24,
    grades: [23, 67, 78, 90, 100],
    calculateAverage: function() {
      const sum = this.grades.reduce((total, grade) => total + grade, 0);
      return sum / this.grades.length;
    }
  };
  
  const student5 = {
    name: "Ziv",
    age: 16,
    grades: [98, 56, 43, 82, 90],
    calculateAverage: function() {
      const sum = this.grades.reduce((total, grade) => total + grade, 0);
      return sum / this.grades.length;
    }
  };
  
  const students = [student1, student2, student3, student4, student5];
  
  students.forEach((student, index) => {
    console.log(`Student ${index}:`);
    console.log(`Name: ${student.name}`);
    console.log(`Age: ${student.age}`);
    console.log(`Grades: ${student.grades.join(', ')}`);
    console.log(`Average Grade: ${student.calculateAverage()}`);
    console.log('                    ');
  });
  
  const adults = students.filter(student => student.age >= 18);
  console.log("Adult Students:");
  console.log(adults);
  
  const myCar = {
    manufacturer: "Nissan",
    model: "Micra",
    year: 2018,
    calculateAge: function() {
      const currentYear = new Date().getFullYear();
      return currentYear - this.year;
    }
  };
  
  console.log("My Car:");
  console.log(`Manufacturer: ${myCar.manufacturer}`);
  console.log(`Model: ${myCar.model}`);
  console.log(`Year: ${myCar.year}`);
  console.log(`Age: ${myCar.calculateAge()} years`);
  