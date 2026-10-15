# Code Smells: Cheat Sheet

Companion to [`smells.txt`](./smells.txt). Use the **index** to scan quickly. Read the
**full entries** when you need the detail: each one has a definition, review
heuristics, legitimate exceptions, smells it's easily confused with, a
before/after example and the named refactorings that fix it.

The examples are deliberately generic. None of them uses an exercise's domain,
so reading this won't spoil an exercise.

**Sources**

| Tag | Work |
|---|---|
| Fowler | Martin Fowler, *Refactoring*, 2nd ed. (2018) |
| Martin | Robert C. Martin, *Clean Code* (2008), ch. 17 "Smells and Heuristics" |
| Wake | William C. Wake, *Refactoring Workbook* (2004) |
| Meszaros | Gerard Meszaros, *xUnit Test Patterns* (2007) |
| van Deursen | van Deursen, Moonen, van den Bergh & Kok, "Refactoring Test Code" (2001) |

Refactoring names in **Fixes** lines come from Fowler's catalogue (2nd ed.) unless
marked otherwise.

---

## Index

### Fowler's core 24

| Smell | In one line |
|---|---|
| [Mysterious Name](#mysterious-name) | You have to read the body to find out what it is or does |
| [Duplicated Code](#duplicated-code) | The same logic in more than one place |
| [Long Function](#long-function) | One function holds several separable ideas |
| [Long Parameter List](#long-parameter-list) | Too many arguments to understand or order correctly |
| [Global Data](#global-data) | Mutable state anyone, anywhere can change |
| [Mutable Data](#mutable-data) | In-place updates with surprising effects at a distance |
| [Divergent Change](#divergent-change) | **One module**, many unrelated reasons to change |
| [Shotgun Surgery](#shotgun-surgery) | **One change**, edits in many modules |
| [Feature Envy](#feature-envy) | A function more interested in another module's data than its own |
| [Data Clumps](#data-clumps) | The same group of values keeps travelling together |
| [Primitive Obsession](#primitive-obsession) | Strings and numbers standing in for domain concepts |
| [Repeated Switches](#repeated-switches) | The same switch on the same type code in several places |
| [Loops](#loops) | Imperative loop where a pipeline would state the intent |
| [Lazy Element](#lazy-element) | Structure that doesn't earn its indirection |
| [Speculative Generality](#speculative-generality) | Flexibility built for a future that hasn't arrived |
| [Temporary Field](#temporary-field) | A field that's only meaningful some of the time |
| [Message Chains](#message-chains) | `a.b().c().d()`: clients coupled to the navigation path |
| [Middle Man](#middle-man) | A class that mostly just forwards calls |
| [Insider Trading](#insider-trading) | Modules swapping knowledge of each other's internals |
| [Large Class](#large-class) | A class doing too much, with clusters of fields inside |
| [Alternative Classes with Different Interfaces](#alternative-classes-with-different-interfaces) | Same job, different method names: not substitutable |
| [Data Class](#data-class) | Fields and accessors only; behaviour lives elsewhere |
| [Refused Bequest](#refused-bequest) | A subclass that doesn't want what it inherits |
| [Comments](#comments) | A comment covering up unclear code |

### Additions

| Smell | In one line | Source |
|---|---|---|
| [Dead Code](#dead-code) | Code that never runs | Wake; Martin G9 |
| [Flag Arguments](#flag-arguments) | A boolean that picks which of two functions to run | Martin F3 |
| [Hidden Temporal Coupling](#hidden-temporal-coupling) | Calls must happen in an order nothing enforces | Martin G31 |
| [Swallowed Exceptions](#swallowed-exceptions) | An error caught and silently dropped | folklore |

### Test smells

| Smell | In one line | Source |
|---|---|---|
| [Obscure Test](#obscure-test) | You can't see what's being verified, or why the expected value follows | Meszaros |
| [Mystery Guest](#mystery-guest) | The test depends on data you can't see in the test | van Deursen; Meszaros |
| [Eager Test](#eager-test) | One test verifies several behaviours | van Deursen; Meszaros |
| [Assertion Roulette](#assertion-roulette) | When it fails, you can't tell which assertion failed or why | van Deursen; Meszaros |
| [Conditional Test Logic](#conditional-test-logic) | `if`/`for`/`try` in a test: some of it may never run | Meszaros |
| [Fragile Test](#fragile-test) | Breaks when the code changes but the behaviour doesn't | Meszaros |
| [Erratic Test](#erratic-test) | Sometimes passes, sometimes fails, with no code change | Meszaros |
| [Slow Tests](#slow-tests) | Slow enough that people stop running them | Meszaros |
| [Test Logic in Production](#test-logic-in-production) | Production code that only exists for the tests | Meszaros; van Deursen |

### Easily-confused pairs

| These two… | …differ like this |
|---|---|
| Divergent Change vs Shotgun Surgery | One module × many kinds of change, vs one change × many modules |
| Feature Envy vs Insider Trading | One function reaching one way for public data, vs two modules entangled in each other's *internals* |
| Message Chains vs Middle Man | Opposite ends of one dial. Hide Delegate fixes chains, but overdo it and you get a Middle Man |
| Lazy Element vs Speculative Generality vs Dead Code | Used but pointless, vs built for a future need, vs never executed |
| Long Parameter List vs Data Clumps vs Primitive Obsession | Too many args, vs args that always travel together, vs values that deserve their own type. Fixes often chain in that order |
| Global Data vs Mutable Data | Global data is mutable data with the widest possible scope |
| Data Class vs Feature Envy | Two sides of one coin: the data class is what's being envied |
| Temporary Field vs Hidden Temporal Coupling | A temporary field is often the *mechanism* that creates the hidden ordering |
| Fragile Test vs Erratic Test | Fails after a harmless code change, vs fails with no change at all |
| Eager Test vs Assertion Roulette | Eager is the cause (too many behaviours), roulette is the symptom (unclear failures) |
| Obscure Test vs Mystery Guest | Mystery Guest is one specific *cause* of an Obscure Test |

---

# Fowler's core 24

## Mysterious Name

*Fowler*

The name of a function, variable, field or class doesn't tell you what it does
or holds, so you have to read its implementation. Fowler: if you can't think of
a good name, that is often a sign of a deeper design problem. The thing may be
doing more than one job.

**Spot it**
- Abbreviations and filler words: `d`, `tmp`, `data`, `info`, `mgr`, `handle`, `process`, `doStuff`
- You can't predict the return value or side effects from the call site
- A name that lies, e.g. `getTotal()` that also writes to the DB

**Not a smell when** the name is conventional in a tiny scope: `i` in a short
loop, `x`/`y` for coordinates, `e` in a `catch`.

**Confused with** [Comments](#comments). A comment explaining a name is a rename waiting to happen.

```python
# Before
def calc(p, r, n):
    return p * (1 + r) ** n
```
```python
# After
def compound_balance(principal, annual_rate, years):
    return principal * (1 + annual_rate) ** years
```

**Fixes** Change Function Declaration · Rename Variable · Rename Field

---

## Duplicated Code

*Fowler*

The same code structure appears in more than one place. Every change has to be
made in each copy, and a reader has to compare the copies to spot the
differences. Near-duplicates count too, and they are worse, because the
differences might be deliberate or might be bugs.

**Spot it**
- Copy-pasted blocks with only names or constants changed
- The same sequence of steps in sibling classes or functions
- A bug fixed in one place that's still live in another

**Not a smell when** the similarity is coincidental: two pieces of code look
alike but change for different reasons. Merging them would couple unrelated
concepts. The rule of three helps here: wait for the third copy if you're unsure.

**Confused with** [Alternative Classes with Different Interfaces](#alternative-classes-with-different-interfaces). That is duplication hidden behind different names.

```js
// Before
function homeTeamPoints(m) {
  if (m.homeGoals > m.awayGoals) return 3;
  if (m.homeGoals === m.awayGoals) return 1;
  return 0;
}
function awayTeamPoints(m) {
  if (m.awayGoals > m.homeGoals) return 3;
  if (m.awayGoals === m.homeGoals) return 1;
  return 0;
}
```
```js
// After
function points(goalsFor, goalsAgainst) {
  if (goalsFor > goalsAgainst) return 3;
  if (goalsFor === goalsAgainst) return 1;
  return 0;
}
const home = points(m.homeGoals, m.awayGoals);
const away = points(m.awayGoals, m.homeGoals);
```

**Fixes** Extract Function · Slide Statements (to line up near-duplicates first) · Pull Up Method

---

## Long Function

*Fowler*

A function that does several separable things. Fowler's point is that length
itself is not the problem. The problem is the gap between *what* the code does
and *how* it does it. His heuristic: whenever you feel the need to comment a
block, extract it into a function named after the comment's intent.

**Spot it**
- Comment headers or blank-line "paragraphs" inside the body
- Deep nesting; many local variables; conditionals with large branches
- A loop that does more than one job

**Not a smell when** the function is long but genuinely does one thing, such as
a declarative table or a flat sequence where every line is already a
well-named call.

**Confused with** [Large Class](#large-class), which is the same problem one level up, and [Loops](#loops).

```python
# Before
def print_receipt(rental):
    # header
    print("=" * 20)
    print("CITY BIKES")
    print("=" * 20)
    # work out cost
    hours = math.ceil((rental.returned - rental.taken).total_seconds() / 3600)
    cost = hours * 3.00
    if hours > 24:
        cost *= 0.8
    # details
    print(f"Bike:  {rental.bike_id}")
    print(f"Hours: {hours}")
    print(f"Cost:  £{cost:.2f}")
```
```python
# After
def print_receipt(rental):
    print_header()
    hours = hours_hired(rental)
    print_details(rental.bike_id, hours, cost_for(hours))

def cost_for(hours):
    cost = hours * 3.00
    return cost * 0.8 if hours > 24 else cost
# print_header, hours_hired, print_details: likewise extracted
```

**Fixes** Extract Function · Replace Temp with Query · Decompose Conditional · Split Loop · Replace Function with Command

---

## Long Parameter List

*Fowler*

So many parameters that callers can't remember their order or meaning.
Adjacent arguments of the same type get silently swapped, and the signature
keeps changing.

**Spot it**
- More than ~3–4 parameters, especially several of the same type in a row
- Callers pull values out of an object they already have, just to pass them in
- Boolean arguments (see [Flag Arguments](#flag-arguments))

**Not a smell when** you're passing values instead of an object *on purpose*,
so the callee doesn't depend on that object's class.

**Confused with** [Data Clumps](#data-clumps). The parameters that always travel together are usually the real fix.

```js
// Before
function searchFlights(origin, destination, departDate, returnDate, adults, children, cabin) { /* … */ }
searchFlights("LHR", "EDI", "2026-05-01", "2026-05-04", 2, 1, "economy");
```
```js
// After
function searchFlights(route, dates, passengers, { cabin = "economy" } = {}) { /* … */ }
searchFlights(
  new Route("LHR", "EDI"),
  new DateRange("2026-05-01", "2026-05-04"),
  { adults: 2, children: 1 },
);
```

**Fixes** Introduce Parameter Object · Preserve Whole Object · Replace Parameter with Query · Remove Flag Argument · Combine Functions into Class

---

## Global Data

*Fowler*

Data that any code anywhere can read **and write**: module-level mutable
variables, class statics and singletons that hold state. When something
changes it, there is no way to find out who did it. It's the most dangerous
form of [Mutable Data](#mutable-data).

**Spot it**
- Module-level mutable `let` / dict / list; the `global` keyword
- A singleton holding state that several features read and write
- Tests that need to reset state between runs (often surfaces as an [Erratic Test](#erratic-test))

**Not a smell when** the data is truly immutable, like constants or frozen
config. Fowler: small doses are tolerable, but the poison scales with the
amount of code that can touch it.

**Confused with** [Mutable Data](#mutable-data).

```python
# Before
current_language = "en"            # any module may reassign this

def greet(name):
    return f"{GREETINGS[current_language]}, {name}"
```
```python
# After: pass it in. If there are too many readers for that, first
# Encapsulate Variable (getter/setter) so every write becomes findable.
def greet(name, language):
    return f"{GREETINGS[language]}, {name}"
```

**Fixes** Encapsulate Variable (first step) · then narrow scope: pass as parameter, move into the owning object

---

## Mutable Data

*Fowler*

Updating data in place can have unexpected effects somewhere else, especially
when several references (aliases) point at the same object. Risk grows with
scope: a mutated local is fine, but a mutated shared object is a bug factory.

**Spot it**
- Functions that mutate their arguments
- One variable reassigned to mean different things over its life
- Stored derived values that have to be kept in sync by hand; setters on things that never legitimately change

**Not a smell when** the mutation is confined to a small local scope, like
building up a local list inside one function.

**Confused with** [Global Data](#global-data) and [Hidden Temporal Coupling](#hidden-temporal-coupling).

```js
// Before
function moveRight(point, dx) {
  point.x += dx;          // mutates the caller's object
  return point;
}
const moved = moveRight(origin, 5);   // surprise: `origin` moved too
```
```js
// After
function moveRight(point, dx) {
  return { ...point, x: point.x + dx };
}
```

**Fixes** Encapsulate Variable · Split Variable · Separate Query from Modifier · Remove Setting Method · Replace Derived Variable with Query · Change Reference to Value · Combine Functions into Transform

---

## Divergent Change

*Fowler*

**One module is changed for several unrelated reasons.** "I change these three
functions whenever the file format changes, and these four whenever the rules
change." The module has more than one responsibility, so unrelated changes
collide in it.

**Spot it**
- `git log` on one file shows a mix of unrelated topics
- A class that mixes persistence, business rules and presentation
- You open the same file for a storage change *and* a display change

**Not a smell when** the "different" reasons always change together in
practice. Then they are one reason.

**Confused with** [Shotgun Surgery](#shotgun-surgery), its mirror image, and [Large Class](#large-class).

```python
# Before
class ChessGame:
    def load_pgn(self, text): ...      # changes when the file format changes
    def legal_moves(self): ...         # changes when rules/variants change
    def render_ascii(self): ...        # changes when the display changes
```
```python
# After
class PgnReader:
    def read(self, text) -> "Position": ...
class Rules:
    def legal_moves(self, position): ...
class AsciiBoard:
    def render(self, position): ...
```

**Fixes** Split Phase · Extract Class · Move Function · Extract Function

---

## Shotgun Surgery

*Fowler*

**One coherent change needs small edits scattered across many modules.** It's
easy to miss one, and the code still runs, just wrongly.

**Spot it**
- Adding one new value (a type, a field, a variant) means touching N files
- "Remember to also update X" in comments, PR templates or tribal knowledge
- A PR that changes one or two lines in each of many files for one feature

**Not a smell when** the edits are in genuinely separate layers you
deliberately keep apart (e.g. migration, API schema, UI). That is a conscious
trade-off. Check that it really is one.

**Confused with** [Divergent Change](#divergent-change). [Repeated Switches](#repeated-switches) is a common cause.

```js
// Before: adding "rabbit" means editing every file
// dosage.js
const mgPerKg = { dog: 5, cat: 2 }[species];                 // rabbit forgotten → undefined dose
// booking.js
const slotMinutes = { dog: 20, cat: 15, rabbit: 10 }[species];
// labels.js
const displayName = { dog: "Dog", cat: "Cat" }[species];     // forgotten here too
```
```js
// After: species.js is the only file to touch
export const SPECIES = {
  dog:    { mgPerKg: 5, slotMinutes: 20, displayName: "Dog" },
  cat:    { mgPerKg: 2, slotMinutes: 15, displayName: "Cat" },
  rabbit: { mgPerKg: 1, slotMinutes: 10, displayName: "Rabbit" },
};
```

**Fixes** Move Function · Move Field · Combine Functions into Class · Combine Functions into Transform · Split Phase · Inline Function / Inline Class (to gather scattered bits first)

---

## Feature Envy

*Fowler*

A function in one module spends more time with the data or functions of
another module than with its own. Fowler's principle: put things together that
change together, so move the behaviour to where the data lives.

**Spot it**
- Lots of `other.x`, `other.y`, `other.z`
- Little or no use of `self` / `this`. The method could almost be static
- When a function envies several modules, it belongs with the one whose data it uses most

**Not a smell when** a pattern separates behaviour from data on purpose
(Strategy, Visitor), or the "envied" data is in a layer you don't want this
behaviour coupled to.

**Confused with** [Insider Trading](#insider-trading) and [Data Class](#data-class) (the envied class is often one). See also [Message Chains](#message-chains).

```python
# Before
class Gardener:
    def compost_litres(self, bed):
        return bed.width * bed.length * bed.depth * 1000 * 0.3
```
```python
# After
class PlantBed:
    def compost_litres(self):
        return self.width * self.length * self.depth * 1000 * 0.3

# Gardener now just calls bed.compost_litres()
```

**Fixes** Move Function · Extract Function (then move only the envious part)

---

## Data Clumps

*Fowler*

The same group of values keeps turning up together: as fields in several
classes, or as parameters in several signatures. Fowler's test: delete one of
the values. Do the others still make sense on their own? If not, they want to
be an object.

**Spot it**
- Repeated tuples: `(start, end)`, `(lat, lng)`, `(amount, currency)`, `(r, g, b)`
- The same parameter group appears in several signatures
- Fields sharing a prefix: `billing_street`, `billing_city`, `billing_postcode`

**Not a smell when** the values only appear together once.

**Confused with** [Long Parameter List](#long-parameter-list) (the symptom) and [Primitive Obsession](#primitive-obsession). Once clumped, give the new object behaviour.

```js
// Before
function blend(r1, g1, b1, r2, g2, b2) { /* … */ }
function toHex(r, g, b) { /* … */ }
function brightness(r, g, b) { /* … */ }
```
```js
// After
class Colour {
  constructor(r, g, b) { Object.assign(this, { r, g, b }); }
  blend(other) { /* … */ }
  toHex() { /* … */ }
  brightness() { /* … */ }
}
```

**Fixes** Extract Class · Introduce Parameter Object · Preserve Whole Object

---

## Primitive Obsession

*Fowler*

Using primitives (strings, numbers, booleans) for domain concepts that deserve
their own type: money, versions, ranges, identifiers, units, type codes. You
lose validation, behaviour and type safety, and the logic for the concept ends
up re-implemented wherever it's used.

**Spot it**
- The same parsing or validation of a string repeated in several places
- Numbers with an implied unit or currency carried elsewhere (or nowhere)
- String/int "type codes" (`"admin"`, `3`) compared in conditionals

**Not a smell when** the value really has no rules or behaviour beyond the
primitive, or you're at a serialisation boundary (JSON in, JSON out).

**Confused with** [Data Clumps](#data-clumps) and [Repeated Switches](#repeated-switches) (switching on a primitive type code).

```python
# Before: version strings parsed ad hoc everywhere
def is_newer(a: str, b: str) -> bool:
    return tuple(map(int, a.split("."))) > tuple(map(int, b.split(".")))

def is_major_bump(old: str, new: str) -> bool:
    return int(new.split(".")[0]) > int(old.split(".")[0])
```
```python
# After
@dataclass(frozen=True, order=True)
class Version:
    major: int
    minor: int
    patch: int

    @classmethod
    def parse(cls, text):
        return cls(*map(int, text.split(".")))

    def is_major_bump_from(self, old):
        return self.major > old.major

# is_newer is now just: new > old
```

**Fixes** Replace Primitive with Object · Replace Type Code with Subclasses · Replace Conditional with Polymorphism · Extract Class · Introduce Parameter Object

---

## Repeated Switches

*Fowler*

The same `switch` / `if-elif` chain on the same discriminator appears in
several places. Adding a case means finding every copy. (The 1st edition
flagged *any* switch statement. The 2nd edition narrows it to *repeated* ones.)

**Spot it**
- `switch (x.kind)` or `if kind == "…"` duplicated across functions
- Adding a new variant turns into [Shotgun Surgery](#shotgun-surgery)
- A `default:` branch that throws "unknown type" in several places

**Not a smell when** there's a single switch in one place, e.g. a factory that
maps input to the right class.

**Confused with** [Primitive Obsession](#primitive-obsession) (the type code being switched on) and [Flag Arguments](#flag-arguments).

```js
// Before
function area(s) {
  switch (s.kind) {
    case "circle": return Math.PI * s.r ** 2;
    case "square": return s.side ** 2;
  }
}
function perimeter(s) {
  switch (s.kind) {
    case "circle": return 2 * Math.PI * s.r;
    case "square": return 4 * s.side;
  }
}
```
```js
// After
class Circle {
  constructor(r) { this.r = r; }
  area() { return Math.PI * this.r ** 2; }
  perimeter() { return 2 * Math.PI * this.r; }
}
class Square {
  constructor(side) { this.side = side; }
  area() { return this.side ** 2; }
  perimeter() { return 4 * this.side; }
}
```
(In functional code, a single dispatch table keyed by `kind` is an equally valid fix.)

**Fixes** Replace Conditional with Polymorphism · Replace Type Code with Subclasses

---

## Loops

*Fowler*

An imperative loop where a collection pipeline (filter/map/reduce,
comprehensions) would state the intent directly. To understand a loop you have
to simulate it in your head. A pipeline names each step.

**Spot it**
- Accumulating into a list or total with an `if` inside the loop
- One loop doing two or three jobs at once
- Index variables that are never really needed

**Not a smell when** the pipeline would be less clear (complex early exits,
state machines), or you're in a hot path where pipeline overhead has actually
been *measured*.

**Confused with** [Long Function](#long-function). A loop doing several things needs Split Loop first.

```python
# Before
names = []
for p in people:
    if p.city == "Leeds":
        names.append(p.name.upper())
```
```python
# After
names = [p.name.upper() for p in people if p.city == "Leeds"]
```

**Fixes** Replace Loop with Pipeline · Split Loop

---

## Lazy Element

*Fowler* (1st ed: "Lazy Class")

A program element (function, class, module, level of hierarchy) that doesn't
pull its weight. It adds indirection without adding meaning. Typical cases: a
function whose body is as clear as its name, or a class that shrank to one
trivial method after refactoring.

**Spot it**
- A function whose body reads the same as its name
- A class with one trivial method and no state
- A subclass or interface layer that adds nothing

**Not a smell when** the name adds meaning the body doesn't (an
intention-revealing wrapper), or the element is a deliberate seam or API
boundary.

**Confused with** [Speculative Generality](#speculative-generality) (built for later; a lazy element shrank or never grew), [Middle Man](#middle-man) and [Dead Code](#dead-code).

```js
// Before
class AreaCalculator {
  rectangle(width, height) { return width * height; }
}
const area = new AreaCalculator().rectangle(width, height);
```
```js
// After
const area = width * height;
```

**Fixes** Inline Function · Inline Class · Collapse Hierarchy

---

## Speculative Generality

*Fowler*

Hooks, abstractions, parameters and special cases added "because we might need
them someday", which nothing uses. You pay for the complexity now for a future
that may never come (YAGNI).

**Spot it**
- An abstract class or interface with exactly one implementation (and no test double)
- Parameters that every caller passes with the same value, or that are ignored
- Fowler: functions or classes whose *only* callers are tests

**Not a smell when** the flexibility is actually used today, or it's required
by a published API or framework contract you don't control.

**Confused with** [Lazy Element](#lazy-element), [Dead Code](#dead-code) and [Test Logic in Production](#test-logic-in-production).

```python
# Before
class ThumbnailStore(ABC):
    @abstractmethod
    def save(self, image, compression=None, replicas=1, encryption_key=None): ...

class DiskThumbnailStore(ThumbnailStore):      # the only implementation
    def save(self, image, compression=None, replicas=1, encryption_key=None):
        image.write(self.path_for(image))      # every option ignored
```
```python
# After
class DiskThumbnailStore:
    def save(self, image):
        image.write(self.path_for(image))
```

**Fixes** Collapse Hierarchy · Inline Function · Inline Class · Change Function Declaration (drop unused params) · Remove Dead Code

---

## Temporary Field

*Fowler*

A field that is only set, or only meaningful, in some circumstances. The rest
of the time it's empty or stale, and readers wonder why it exists. It's often
a set of fields a complicated algorithm uses to avoid passing parameters.

**Spot it**
- Fields that are `None`/`undefined` except during one method call
- `if self._x is not None` checks scattered around
- One method sets a field purely so that a helper it calls can read it

**Not a smell when** the value is a genuinely optional attribute of the domain
(a middle name, an optional delivery note).

**Confused with** [Hidden Temporal Coupling](#hidden-temporal-coupling), which temporary fields often cause, and [Data Clumps](#data-clumps).

```js
// Before
class SpellChecker {
  check(text) {
    this.words = text.split(/\s+/);   // only meaningful during check()
    this.errors = [];
    this.#scan();
    return this.errors;
  }
  #scan() {
    for (const w of this.words) if (!DICTIONARY.has(w)) this.errors.push(w);
  }
}
```
```js
// After: pass data explicitly. For a bigger algorithm, extract a class whose
// whole lifetime *is* the computation (Replace Function with Command).
class SpellChecker {
  check(text) {
    return text.split(/\s+/).filter((w) => !DICTIONARY.has(w));
  }
}
```

**Fixes** Extract Class · Replace Function with Command · Move Function · Introduce Special Case (for the "not set" branch)

---

## Message Chains

*Fowler*

A client asks one object for another, then asks that object for another, and
so on: `a.getB().getC().getD()`. The client is now coupled to the entire
navigation path, and any change to an intermediate relationship breaks it.
(This is what the Law of Demeter guards against.)

**Spot it**
- Long dot chains through *different* kinds of object
- The same chain repeated in several places
- A client that knows how three or four classes connect to each other

**Not a smell when** it's a fluent interface or pipeline returning the same
kind of thing (`list.filter().map()`, builders), or you're walking plain data
(JSON, DTOs) whose structure *is* the contract.

**Confused with** [Middle Man](#middle-man). Fixing chains with Hide Delegate can overshoot into it.

```python
# Before
phone = appointment.doctor.clinic.manager.phone
```
```python
# After: ask "what does the client actually want?" and put that on the
# nearest object.
class Appointment:
    def escalation_contact(self):
        return self.doctor.escalation_contact()

phone = appointment.escalation_contact().phone
```

**Fixes** Hide Delegate · Extract Function (the code that uses the chain) · Move Function (push it down the chain)

---

## Middle Man

*Fowler*

A class whose methods mostly just delegate to another class. Encapsulation has
gone too far, and the class adds indirection without adding value. Every new
feature on the delegate needs a new forwarding method here too.

**Spot it**
- Most methods are one-line forwarders to the same field
- Adding a feature to the delegate means adding a forwarder here
- Clients would be simpler talking to the delegate directly

**Not a smell when** it's a deliberate Facade, Proxy, Adapter, Decorator or
anti-corruption layer. Each of those adds simplification, control, translation
or a boundary.

**Confused with** [Message Chains](#message-chains), the other end of the same dial, and [Lazy Element](#lazy-element).

```js
// Before
class Driver {
  constructor(car) { this.car = car; }
  get fuelLevel()      { return this.car.fuelLevel; }
  get mileage()        { return this.car.mileage; }
  get tyrePressure()   { return this.car.tyrePressure; }
  get nextServiceDue() { return this.car.nextServiceDue; }
}
```
```js
// After
class Driver {
  constructor(car) { this.car = car; }
}
// clients: driver.car.mileage
```

**Fixes** Remove Middle Man · Inline Function · Replace Superclass with Delegate · Replace Subclass with Delegate

---

## Insider Trading

*Fowler* (1st ed: "Inappropriate Intimacy")

Modules that trade a lot of knowledge about each other's internals behind the
scenes. This couples them so tightly that you can't change one without the
other. Subclasses that know too much about their parent's internals also count.

**Spot it**
- Reaching into another class's private or `_underscore` fields
- Two classes calling each other's internals in both directions
- A subclass manipulating its parent's protected state directly

**Not a smell when** a tightly-knit pair is deliberately kept inside one
module boundary (e.g. a collection and its iterator).

**Confused with** [Feature Envy](#feature-envy) (one function, one direction, usually public data).

```python
# Before
class Transfer:
    def run(self, src, dst, amount):
        src._balance -= amount
        dst._balance += amount
        src._history.append(("out", amount))
        dst._history.append(("in", amount))
```
```python
# After
class Account:
    def withdraw(self, amount):
        self._balance -= amount
        self._history.append(("out", amount))
    def deposit(self, amount):
        self._balance += amount
        self._history.append(("in", amount))

class Transfer:
    def run(self, src, dst, amount):
        src.withdraw(amount)
        dst.deposit(amount)
```

**Fixes** Move Function · Move Field · Hide Delegate · Replace Subclass with Delegate · Replace Superclass with Delegate

---

## Large Class

*Fowler*

A class doing too much: too many fields, too many methods, too much code. It's
a breeding ground for duplication and [Divergent Change](#divergent-change).
Size alone isn't the criterion. Look for **clusters** of fields and methods
that only use each other.

**Spot it**
- Groups of fields with a shared prefix or suffix (`position_x`, `position_y`)
- Subsets of methods that only touch subsets of fields
- Several unrelated reasons to change the class (see [Divergent Change](#divergent-change))

**Not a smell when** the class is big but cohesive, with most methods using
most fields. That's rare, so check before you excuse it.

**Confused with** [Divergent Change](#divergent-change), [Data Clumps](#data-clumps) (prefix-grouped fields) and [Long Function](#long-function).

```python
# Before
class Player:
    name: str
    position_x: float
    position_y: float
    velocity_x: float
    velocity_y: float
    inventory_items: list
    inventory_capacity: int
    def move(self, dt): ...
    def bounce(self): ...
    def pick_up(self, item): ...
    def drop(self, item): ...
```
```python
# After
class Body:
    x: float; y: float; vx: float; vy: float
    def move(self, dt): ...
    def bounce(self): ...

class Inventory:
    items: list; capacity: int
    def add(self, item): ...
    def remove(self, item): ...

class Player:
    name: str
    body: Body
    inventory: Inventory
```

**Fixes** Extract Class · Extract Superclass · Replace Type Code with Subclasses

---

## Alternative Classes with Different Interfaces

*Fowler*

Two classes do the same job but expose different method names or signatures,
so you can't substitute one for the other. Clients end up branching on which
one they have.

**Spot it**
- `send(to, body)` in one class vs `dispatchMessage(body, recipient)` in another
- Client code that does `if instanceof A … else …` to call the "same" thing
- Duplicated client logic adapting each one

**Not a smell when** the similarity is only skin-deep and the two have
genuinely different contracts.

**Confused with** [Duplicated Code](#duplicated-code) and [Repeated Switches](#repeated-switches) (clients switching on which class they have).

```js
// Before
class FileLogger    { write(line) { /* … */ } }
class ConsoleLogger { print(level, text) { /* … */ } }

if (logger instanceof FileLogger) logger.write(`[${level}] ${text}`);
else logger.print(level, text);
```
```js
// After
class FileLogger    { log(level, text) { /* … */ } }
class ConsoleLogger { log(level, text) { /* … */ } }

logger.log(level, text);
```

**Fixes** Change Function Declaration · Move Function (until the protocols match) · Extract Superclass (if they now share code)

---

## Data Class

*Fowler*

A class with fields and getters/setters and nothing else. Other classes
manipulate its data, so behaviour that belongs with the data lives somewhere
else, often duplicated.

**Spot it**
- Only fields and accessors; public setters for everything
- Logic about its fields repeated in client classes (they show [Feature Envy](#feature-envy) towards it)
- Clients compute the same derived value from its fields

**Not a smell when** it's a result record, e.g. the output of Split Phase, or a
DTO at a system boundary, *especially* if it's immutable. Fowler explicitly
exempts these. Value objects are also fine.

**Confused with** [Feature Envy](#feature-envy), the other side of the same coin.

```python
# Before
@dataclass
class Flight:
    departs: datetime
    arrives: datetime

# departures_board.py
minutes = (f.arrives - f.departs).total_seconds() / 60
# itinerary.py
minutes = (f.arrives - f.departs).total_seconds() / 60
```
```python
# After
@dataclass(frozen=True)
class Flight:
    departs: datetime
    arrives: datetime

    def duration_minutes(self):
        return (self.arrives - self.departs).total_seconds() / 60
```

**Fixes** Encapsulate Record · Remove Setting Method · Move Function · Extract Function

---

## Refused Bequest

*Fowler*

A subclass inherits methods or data it doesn't want or can't support. There's
a mild form and a strong form. In the mild form it just ignores some of what
it inherits, which Fowler says is often not worth fixing. In the strong form
it **refuses the superclass's interface** by overriding methods to throw or do
nothing, which breaks substitutability (Liskov).

**Spot it**
- Overrides that throw `NotImplementedError` or do nothing
- A subclass that uses only a small fraction of its parent
- Inheritance used for code reuse rather than a true "is-a" relationship

**Not a smell when** the subclass merely doesn't use some *implementation*
while still honouring the *interface*.

**Confused with** [Middle Man](#middle-man). Replacing inheritance with delegation can overshoot into one.

```js
// Before
class Bird {
  fly() { /* … */ }
  layEgg() { /* … */ }
}
class Penguin extends Bird {
  fly() { throw new Error("Penguins can't fly"); }
}
```
```js
// After
class Bird { layEgg() { /* … */ } }
class FlyingBird extends Bird { fly() { /* … */ } }
class Penguin extends Bird {}
```

**Fixes** Push Down Method · Push Down Field · Replace Subclass with Delegate · Replace Superclass with Delegate

---

## Comments

*Fowler*

Comments are not bad in themselves. The smell is a comment used as
*deodorant*, explaining *what* the code does because the code doesn't say it.
Fowler: "When you feel the need to write a comment, first try to refactor the
code so that any comment becomes superfluous."

**Spot it**
- A comment that restates the next line or labels a block (extract it)
- A comment explaining what a variable or function name means (rename it)
- A comment stating a precondition (make it an assertion); commented-out code (see [Dead Code](#dead-code))

**Not a smell when** the comment explains *why*: a non-obvious decision, a
workaround with a bug link, a performance trade-off, a legal notice, or API
docs.

**Confused with** [Mysterious Name](#mysterious-name), [Long Function](#long-function) and [Dead Code](#dead-code).

```python
# Before
# check if person can vote
if p.age >= 18 and p.is_citizen and p.registered_at is not None:
    ...
```
```python
# After
if person.can_vote():
    ...
```

**Fixes** Extract Function · Change Function Declaration · Introduce Assertion

---

# Additions

## Dead Code

*Wake (Refactoring Workbook); Martin G9.* Fowler covers the fix as Remove Dead Code.

Code that never executes: unused functions, variables, parameters and imports;
unreachable branches; commented-out blocks. You still pay to read it, maintain
it and search past it, and it misleads people about what the system does.

**Spot it**
- No callers (IDE "find usages", grep, coverage reports)
- Branches guarded by conditions that can't occur (validated away upstream)
- Commented-out code; unused parameters and imports

**Not a smell when** it's public API used by consumers you can't see, or it's
reached through reflection or dynamic dispatch. Check before you delete.

**Confused with** [Speculative Generality](#speculative-generality) (written for later, still "live" in the type system) and [Lazy Element](#lazy-element) (used, but pointless).

```js
// Before
function brewSeconds(tea) {
  if (tea.type === "green") return 120;
  if (tea.type === "black") return 240;
  if (tea.type === "coffee") return 0;  // impossible: type is validated to green/black/herbal
  // return tea.strength * 60;          // old formula
  return 300;
}
function legacyBrewTable() { /* no callers */ }
```
```js
// After
function brewSeconds(tea) {
  if (tea.type === "green") return 120;
  if (tea.type === "black") return 240;
  return 300;
}
```

**Fixes** Remove Dead Code. Version control remembers it if you ever need it back.

---

## Flag Arguments

*Martin F3:* "Boolean arguments loudly declare that the function does more than one thing."

A boolean (or small enum) parameter that selects which branch of the function
runs. The call site `render(doc, true)` tells the reader nothing, and the
function is really two functions glued together.

**Spot it**
- Literal `true`/`false` at call sites
- A function body that is basically `if flag: A else: B`
- Several flags together, which multiply the hidden code paths

**Not a smell when** the boolean is *data* passed through rather than a
choice of control flow, e.g. `set_visible(is_visible)` where the value comes
from a variable. Fowler makes the same distinction.

**Confused with** [Long Parameter List](#long-parameter-list) and [Repeated Switches](#repeated-switches).

```python
# Before
def format_name(person, surname_first):
    if surname_first:
        return f"{person.surname}, {person.given}"
    return f"{person.given} {person.surname}"

format_name(p, True)
```
```python
# After
def full_name(person):
    return f"{person.given} {person.surname}"

def sortable_name(person):
    return f"{person.surname}, {person.given}"

sortable_name(p)
```

**Fixes** Remove Flag Argument · Replace Conditional with Polymorphism (when the flag is really a type)

---

## Hidden Temporal Coupling

*Martin G31*

Methods must be called in a particular order, but nothing in the code shows or
enforces that order. Call them out of order, or skip one, and you get a subtle
bug instead of a compile error or an obvious crash.

**Spot it**
- Methods that read fields set by other methods
- `init()` / `open()` / `prepare()` that "must be called first"
- Comments like "call X before Y"; objects that are only valid after a setup call

**Not a smell when** the order is enforced structurally: each step returns
what the next one needs, a builder only yields a ready object, or a context
manager / `try-finally` owns the lifecycle.

**Confused with** [Temporary Field](#temporary-field), often the mechanism, and [Mutable Data](#mutable-data).

```python
# Before
class Compiler:
    def compile(self, source):
        self.parse(source)     # sets self.ast
        self.type_check()      # reads self.ast, sets self.types
        return self.emit()     # reads self.ast and self.types
```
```python
# After: Martin's "bucket brigade". Each step needs the previous result,
# so it can't be reordered.
class Compiler:
    def compile(self, source):
        ast = self.parse(source)
        types = self.type_check(ast)
        return self.emit(ast, types)
```

**Fixes** Pass results explicitly (bucket brigade) · Split Phase · Builder or constructor that returns a ready-to-use object · Context manager for open/close pairs

---

## Swallowed Exceptions

*Folklore*

An exception is caught and ignored, or merely logged, and the program carries
on as if it had succeeded. The failure becomes invisible, the program goes on
in a corrupt state, and whoever debugs it later has nothing to go on.

**Spot it**
- `except: pass`, `catch (e) {}`, `catch (e) { /* ignore */ }`
- `catch (e) { console.log(e) }` followed by business as usual
- A broad `catch (Exception)` around a large block, returning a default value

**Not a smell when** the exception is genuinely expected and handled
meaningfully: a narrow type, a deliberate recovery, a stated reason. Example:
`FileNotFoundError` → use default settings.

**Confused with** [Conditional Test Logic](#conditional-test-logic). A `try/catch` in a test swallows failures the same way.

```js
// Before
async function deleteAvatar(userId) {
  try {
    await fs.unlink(avatarPath(userId));
  } catch (e) {}
}
```
```js
// After
async function deleteAvatar(userId) {
  try {
    await fs.unlink(avatarPath(userId));
  } catch (e) {
    if (e.code === "ENOENT") return;   // already gone, which is the outcome we wanted
    throw e;
  }
}
```

**Fixes** Let it propagate (often you can just delete the `try`) · Catch the narrowest type · Wrap in a domain exception that keeps the `cause` · Handle with a real recovery

---

# Test smells

## Obscure Test

*Meszaros*

You can't tell at a glance what a test is verifying, or why the expected value
follows from the setup. Common causes are irrelevant detail in the setup, a
[Mystery Guest](#mystery-guest), an [Eager Test](#eager-test), magic numbers,
and testing indirectly through other objects.

**Spot it**
- A long arrange section full of fields that don't affect the outcome
- Magic numbers in assertions with no visible derivation
- A vague test name like `test_fare` or `it works`

**Not a smell when** the behaviour is inherently complex. Even then, hide the
*incidental* detail so the essential detail stands out.

**Confused with** [Mystery Guest](#mystery-guest) and [Eager Test](#eager-test), which are both causes.

```python
# Before
def test_fare():
    p = Passenger("P-001", "Ann", "Lee", "ann@example.com", "GB",
                  date(1955, 4, 2), "window", False, 3)
    b = Booking(p, Flight("LHR", "EDI", date(2026, 5, 1), 120.00))
    assert b.fare() == 96.00
```
```python
# After
def test_passengers_over_65_get_20_percent_off():
    booking = a_booking(passenger=a_passenger(age=70), base_fare=120.00)
    assert booking.fare() == 120.00 * 0.8
```

**Fixes** Creation Method / Test Data Builder (Meszaros) · Intention-revealing test names · Derived Value in the assertion · Custom Assertion · Fresh Fixture built in the test (instead of a General Fixture)

---

## Mystery Guest

*van Deursen et al.; Meszaros (as a cause of Obscure Test)*

The test depends on an external resource whose contents aren't visible in the
test: a fixture file, seeded DB rows, an env var, or a shared setup somewhere
else. You can't see cause and effect without going to look elsewhere.

**Spot it**
- The test loads `fixtures/whatever.json` or relies on seed data
- Magic IDs (`get_user(42)`) that only mean something in another file
- Assertions on values that appear nowhere in the test

**Not a smell when** it's an approval or snapshot test where the file *is*
the expected output and is reviewed alongside the code.

**Confused with** [Obscure Test](#obscure-test) (the umbrella) and [Erratic Test](#erratic-test) (shared external resources also cause flakiness).

```js
// Before
test("finds active users", () => {
  const users = loadUsers("fixtures/users.json");
  expect(activeUsers(users)).toHaveLength(3);   // which 3? why?
});
```
```js
// After
test("users who logged in within 30 days are active", () => {
  const users = [
    { name: "ann", lastLogin: "2026-09-30" },
    { name: "bob", lastLogin: "2024-01-01" },
  ];
  const active = activeUsers(users, { today: "2026-10-01" });
  expect(active.map((u) => u.name)).toEqual(["ann"]);
});
```

**Fixes** Inline Resource · Set up the external resource inside the test · Creation Method (Meszaros)

---

## Eager Test

*van Deursen et al.; Meszaros (as a cause of Assertion Roulette)*

A single test verifies several distinct behaviours. When it fails, you don't
know which behaviour broke, and the assertions after the first failure never
run. The test name can't describe what it checks.

**Spot it**
- Several act → assert cycles in one test
- Names like `test_stack`, `test_everything`, or a name containing "and"
- You have to read the whole test to work out what it's for

**Not a smell when** several assertions check *one* outcome, e.g. multiple
fields of a single returned object.

**Confused with** [Assertion Roulette](#assertion-roulette), its usual symptom, and [Obscure Test](#obscure-test).

```python
# Before
def test_stack():
    s = Stack()
    assert s.is_empty()
    s.push(1)
    s.push(2)
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.pop() == 1
    with pytest.raises(EmptyStackError):
        s.pop()
```
```python
# After
def test_new_stack_is_empty(): ...
def test_peek_returns_last_pushed(): ...
def test_pop_returns_items_in_lifo_order(): ...
def test_pop_on_empty_stack_raises(): ...
```

**Fixes** Split into Single-Condition Tests (Meszaros) · Extract shared setup into a fixture or helper

---

## Assertion Roulette

*van Deursen et al.; Meszaros*

A test has many assertions, and when one fails the output doesn't tell you
which one or why. Meszaros gives two causes: [Eager Test](#eager-test) and
missing assertion messages.

**Spot it**
- A run of bare `assertTrue(...)` / `expect(cond).toBe(true)` lines
- Failure output like "expected true, received false"
- Several assertions with similar-looking values

**Not a smell when** your framework already reports the failing expression and
both values. pytest's assertion rewriting and Jest's `toEqual` diffs largely
defuse it. Boolean-style assertions still bite, though.

**Confused with** [Eager Test](#eager-test).

```js
// Before
test("parses URL", () => {
  const u = parseUrl("https://example.com:8080/a/b");
  expect(u.scheme === "https").toBe(true);
  expect(u.host === "example.com").toBe(true);
  expect(u.port === 8080).toBe(true);
  expect(u.path === "/a/b").toBe(true);
});
// failure: "expected true, received false". Which one?
```
```js
// After
test("parses URL", () => {
  expect(parseUrl("https://example.com:8080/a/b")).toEqual({
    scheme: "https", host: "example.com", port: 8080, path: "/a/b",
  });
});
```

**Fixes** Compare whole objects (Expected Object) · Custom Assertion · Assertion Message · Split the test (if it's also an Eager Test)

---

## Conditional Test Logic

*Meszaros*

A test contains `if`, loops, or `try/catch`, which means code that might not
run. The test can then pass without verifying anything, and the test itself
becomes logic that needs testing.

**Spot it**
- An `if` around an assertion
- A `for` loop with assertions inside, which passes vacuously on an empty collection
- `try/except` in a test body (a [Swallowed Exception](#swallowed-exceptions) in disguise)

**Not a smell when** the logic is inside a test *utility* that is itself
tested, or you're using the framework's parameterisation feature.

**Confused with** [Swallowed Exceptions](#swallowed-exceptions) and [Obscure Test](#obscure-test).

```python
# Before
def test_admins_have_2fa():
    for user in api.list_users():   # empty list → passes, verifying nothing
        if user.is_admin:
            assert user.has_2fa
```
```python
# After
def test_creating_an_admin_enables_2fa():
    user = api.create_user(role="admin")
    assert user.has_2fa

# for several cases, parameterise instead of looping:
@pytest.mark.parametrize("role, expected", [("admin", True), ("viewer", False)])
def test_2fa_by_role(role, expected):
    assert api.create_user(role=role).has_2fa is expected
```

**Fixes** Parameterized Test · Guard Assertion · Custom Assertion · Fresh Fixture with known data

---

## Fragile Test

*Meszaros*

A test breaks when the production code changes in a way that **doesn't alter
the behaviour under test**. Meszaros's causes are sensitivity to the interface,
to unrelated behaviour, to data and to context, plus "overspecified software"
(mocks asserting every interaction).

**Spot it**
- A pure refactoring turns tests red
- Assertions on private methods, call counts, exact SQL/log/HTML strings
- Strict mocks verifying every collaborator call

**Not a smell when** the test failed because the behaviour really did change.
That's the test doing its job.

**Confused with** [Erratic Test](#erratic-test). Fragile fails *after a change*; Erratic fails *without one*.

```python
# Before
def test_get_user():
    db = Mock()
    db.execute.return_value.fetchone.return_value = (7, "Ann")
    UserService(db).get(7)
    db.execute.assert_called_once_with("SELECT id, name FROM users WHERE id = 7")
    # reformat the SQL or switch to a bound parameter → red, though nothing broke
```
```python
# After: verify the outcome, not the implementation
def test_get_returns_stored_user():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (id INTEGER, name TEXT)")
    db.execute("INSERT INTO users VALUES (7, 'Ann')")
    assert UserService(db).get(7) == User(7, "Ann")
```

**Fixes** Test through the public interface · Fakes/stubs over strict mocks (assert outcomes, not interactions) · Creation Methods to absorb constructor churn · Assert only what the test is about

---

## Erratic Test

*Meszaros*

A test that sometimes passes and sometimes fails with **no code change**: a
"flaky" test. Meszaros's causes include interacting tests (shared state, order
dependence), resource leakage, unrepeatable tests, parallel test-run wars, and
non-determinism (clock, randomness, threads, network).

**Spot it**
- "Just re-run CI"
- Passes alone but fails in the full suite (or the reverse, or only in parallel)
- Uses `now()`, `random`, `sleep`, a real network, or a shared database

**Not a smell when** never. Flakiness always costs trust. Quarantine is a
stopgap, not a fix.

**Confused with** [Fragile Test](#fragile-test). [Global Data](#global-data) and [Mystery Guest](#mystery-guest) are common causes.

```python
# Before
def test_publish_sets_todays_date():
    post = Post("Hello")
    post.publish()                              # calls datetime.now() inside
    assert post.published_on == date.today()    # fails if run across midnight
```
```python
# After: inject the clock
def test_publish_uses_current_date_from_clock():
    clock = lambda: datetime(2026, 3, 1, 23, 59, 59)
    post = Post("Hello", clock=clock)
    post.publish()
    assert post.published_on == date(2026, 3, 1)
```

**Fixes** Inject clock / random seed · Fresh Fixture per test · Clean up resources (teardown) · Remove shared mutable state · Replace network/IO with test doubles

---

## Slow Tests

*Meszaros*

The suite takes long enough that developers stop running it often, which
kills the fast feedback that makes refactoring and TDD work. Typical causes:
real DB, network or filesystem calls; `sleep`-based waits; expensive per-test
setup; too many end-to-end tests.

**Spot it**
- `sleep` / `setTimeout` waits in tests
- Every test spins up a real DB or the whole app
- People run "just this one file" because the whole suite takes minutes

**Not a smell when** a deliberately slow tier (integration/e2e) is kept
separate and run less often, while the fast unit suite stays fast.

**Confused with** [Erratic Test](#erratic-test). Real-time waits cause both.

```js
// Before: 600 ms of real waiting, per test
test("searches once after typing stops", async () => {
  const search = jest.fn();
  const box = new SearchBox(search, { debounceMs: 500 });
  box.type("c"); box.type("ca"); box.type("cat");
  await new Promise((r) => setTimeout(r, 600));
  expect(search).toHaveBeenCalledTimes(1);
});
```
```js
// After: fake timers, so it takes effectively no time
test("searches once after typing stops", () => {
  jest.useFakeTimers();
  const search = jest.fn();
  const box = new SearchBox(search, { debounceMs: 500 });
  box.type("c"); box.type("ca"); box.type("cat");
  jest.advanceTimersByTime(500);
  expect(search).toHaveBeenCalledTimes(1);
  expect(search).toHaveBeenCalledWith("cat");
});
```

**Fixes** Fake clock/timers · Test doubles or in-memory fakes for IO · Shared *immutable* fixture for expensive setup · Push tests down the pyramid

---

## Test Logic in Production

*Meszaros; van Deursen et al. call a variant "For Testers Only"*

Production code that exists only for the tests: `if TESTING` branches, test
hooks, methods only tests call, flags that bypass validation. It can be
switched on in production by accident, it means the real path is the one
that goes untested, and it clutters the code.

**Spot it**
- `if os.environ.get("TESTING")`, `if (process.env.NODE_ENV === "test")`
- Parameters like `skip_validation=False` that only tests ever set
- Methods named `…_for_test` or `reset()` used only by tests

**Not a smell when** it's a genuine seam: dependency injection through a
constructor parameter with a production default. That's the *fix*, not the
smell.

**Confused with** [Speculative Generality](#speculative-generality) (code whose only callers are tests) and [Flag Arguments](#flag-arguments).

```python
# Before
def translate(text, lang):
    if os.environ.get("TESTING"):
        return text.upper()                     # fake behaviour lives in prod
    return requests.post(API, json={"q": text, "to": lang}).json()["text"]
```
```python
# After: inject the dependency; the fake lives in the test
class Translator:
    def __init__(self, http=requests):
        self.http = http

    def translate(self, text, lang):
        return self.http.post(API, json={"q": text, "to": lang}).json()["text"]

# test:
translator = Translator(http=FakeHttp({"text": "bonjour"}))
```

**Fixes** Dependency Injection · Test Double (stub/fake) supplied by the test · Test-Specific Subclass (Meszaros) · Delete test-only branches and hooks
