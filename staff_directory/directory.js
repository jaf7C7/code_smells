class Building {
  constructor(name, address) {
    this.name = name;
    this.address = address;
  }

  getName() {
    return this.name;
  }

  getAddress() {
    return this.address;
  }
}

class Office {
  constructor(floor, building) {
    this.floor = floor;
    this.building = building;
  }

  getFloor() {
    return this.floor;
  }

  getBuilding() {
    return this.building;
  }
}

class Employee {
  constructor(name, office, department = null) {
    this.name = name;
    this.office = office;
    this.department = department;
  }

  getOffice() {
    return this.office;
  }

  getDepartment() {
    return this.department;
  }
}

class Department {
  constructor(name, head) {
    this.name = name;
    this.head = head;
  }

  getHead() {
    return this.head;
  }
}

function managerMailingAddress(employee) {
  return employee.getDepartment().getHead().getOffice().getBuilding().getAddress();
}

function managerFloor(employee) {
  return employee.getDepartment().getHead().getOffice().getFloor();
}

function worksInSameBuildingAsManager(employee) {
  return (
    employee.getOffice().getBuilding().getName() ===
    employee.getDepartment().getHead().getOffice().getBuilding().getName()
  );
}

module.exports = { Building, Office, Employee, Department, managerMailingAddress, managerFloor, worksInSameBuildingAsManager };
