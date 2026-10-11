const {
  Building,
  Office,
  Employee,
  Department,
  managerMailingAddress,
  managerFloor,
  worksInSameBuildingAsManager,
} = require('./directory');

const tower = new Building('Tower', '1 High Street');
const annexe = new Building('Annexe', '3 Back Lane');
const head = new Employee('Grace', new Office(7, tower));
const engineering = new Department('Engineering', head);

describe('directory', () => {
  test("finds the address of an employee's manager", () => {
    const ada = new Employee('Ada', new Office(2, annexe), engineering);
    expect(managerMailingAddress(ada)).toBe('1 High Street');
  });

  test("finds the floor of an employee's manager", () => {
    const ada = new Employee('Ada', new Office(2, annexe), engineering);
    expect(managerFloor(ada)).toBe(7);
  });

  test('knows when an employee works in a different building from their manager', () => {
    const ada = new Employee('Ada', new Office(2, annexe), engineering);
    expect(worksInSameBuildingAsManager(ada)).toBe(false);
  });

  test('knows when an employee works in the same building as their manager', () => {
    const alan = new Employee('Alan', new Office(3, tower), engineering);
    expect(worksInSameBuildingAsManager(alan)).toBe(true);
  });
});
