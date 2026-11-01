# Qatalyst: from scientific abstracts to executable experiments

An abstract is a starting point. Qatalyst brings ideas, code, simulation, and critique into one inspectable loop for Algorithm Discovery for Science.

**MIT Science Hackathon · Algorithm Discovery for Science**

**Team:** Sanjay Das, Ethan Seefried, Chris, Tahisha, Shaziaviedi

[Source code](https://github.com/eseefried/Algo-Discovery-Sim) · [Architecture notes](https://github.com/eseefried/Algo-Discovery-Sim/blob/main/docs/architecture.md)

## An idea deserves an experiment

Imagine reading a short description of a quantum algorithm and asking: can we turn this into something we can actually test? That gap—from a promising idea to an executable experiment—is the starting point for Qatalyst, our MIT Science Hackathon project within Algorithm Discovery for Science. Our goal is to make scientific reasoning actionable, inspectable, and easier to build upon.

![Qatalyst architecture: shared task ledger, researcher and reviewer agents, Nemotron and Sonnet services, Qiskit simulation, and energy-based replacement.](assets/blog/qatalyst-architecture.png)

Native hybrid architecture from the project repository. Click to open the full-resolution diagram.

## A research team in a shared workspace

Qatalyst’s lobster-themed architecture gives cooperating AI agents a shared task ledger: candidate methods, feedback, virtual energy, and lineage. In the native hybrid, two agents can develop implementations while a third remains outside their implementation chains for review. Local Nemotron proposes numbered equations; Sonnet assembles plans and specifications, writes Qiskit code, and reviews results. Docker and Qiskit Aer provide the build-and-simulation stage. Failed or questioned candidates return for revision; depleted agents can be replaced. Review is a checkpoint, and independent functional tests remain essential.

## Three ways to organize the work

The completed Sonnet study compares a single specification-writing agent, a three-worker ledger swarm, and Abstract2Method: a search swarm starting with six agents and allowing up to ten. All use a shared final code stage. A separate, newer hybrid combines a fine-tuned NVIDIA Nemotron Bolt equation generator with Sonnet coordination and review. The local adapter is trained for abstract-to-numbered-LaTeX generation; the hybrid is not an all-local system. These configurations let us ask when coordination helps, how much it costs, and which scientific checks it still needs.

## What the completed benchmark tells us

Across the same 84 papers and 320 labelled main equations, single-agent Sonnet recovered 54 matching equations, compared with 26 for the ledger swarm and 46 for Abstract2Method. Across all 96 attempted papers, Abstract2Method reached simulation on 93, compared with 77 for the single agent and 48 for the ledger. Estimated API totals were $7.52, $13.67, and $61.97 respectively. Single-agent Sonnet offered the strongest measured cost–math tradeoff; Abstract2Method produced more runnable circuits at about 8.2 times the total cost. Equation similarity measures textual and structural matching, and simulation yield measures execution. Neither establishes full algorithm correctness.

## Example 1 · Find the marked answer

Think of sixteen labelled cards with one marked answer. Grover search amplifies the probability of measuring that answer. In a saved four-qubit example, Qatalyst generated and simulated a circuit with marked value 5, written 0101 in binary, and three iterations. The target received 96.13% of the simulated probability; each other state received about 0.258%. The candidate completed execution and agent review in 156.33 seconds at an estimated $0.2543 in paid usage. This illustrates a complete proposal–repair–execution–review path for one instance; it does not establish the source paper’s broader gate-error claims.

![Grover simulation: target 0101 has 96.13 percent probability, versus 3.87 percent shared by the other fifteen states.](assets/blog/qatalyst-grover.svg)

One saved four-qubit simulation, not a general algorithm-correctness score. Values from the supplied November 1 report.

## Example 2 · Recover a hidden rule

An affine Boolean function is a compact hidden rule: f(x) = a·x ⊕ b. Here a selects which input bits matter, and b flips the output. In a separate corrected hybrid pilot, the generated method recovered both hidden components in 28 of 28 tested parameter instances across one to three data qubits. For n = 2, a = 1, b = 1, the simulator returned 101 in all 1,024 shots. The oracle parameters are explicit gate-construction inputs, and controlled-phase-oracle access is assumed. This is evidence for the tested finite contract, rather than black-box query complexity or a new mathematical discovery.

## The hybrid snapshot: promising engineering, open attribution

The November 1, 2026 report records 21 completed papers out of 65 planned in the hybrid batch. Fifteen reached reviewed-ready status: execution plus approval by another agent outside the implementation chain. Median per-paper time was 156.33 seconds; estimated paid Sonnet usage totalled $6.14. These partial-batch outcomes are separate from the completed Sonnet benchmark. None of the selected candidates’ assembled equations retained native proposals verbatim. Sonnet supplied substantial reconstruction and repair; a matched Sonnet-only ablation is needed to establish Nemotron’s incremental contribution. Local hardware and serving costs are excluded.

## A useful failure points to the next experiment

For a small N = 15 order-finding instance, code built and simulated, but review questioned the consistency of work-register initialization. The run ended without an approved candidate after two energy-depletion deaths and two replacements. The objection was not independently reproduced as a valid-instance numerical counterexample, so this remains unresolved. Preserving that distinction is part of scientific rigor: a running circuit, an agent’s approval, and a validated scientific result are different milestones.

## Built with a practical AI toolkit

The team used NVIDIA ALCHEMI, Sonnet for single-agent and swarm experiments, and a fine-tuned NVIDIA Nemotron Bolt model for local equation generation in the hybrid swarm. Claude and GPT Sol supported the build. We acknowledge the $100 in Claude API support provided for building the project. This support is distinct from the report’s usage-based experiment-cost estimates. The supplied report evaluates quantum reconstruction; it does not isolate an ALCHEMI performance contribution.

## Our mission: a shorter path from question to evidence

SuperIntelligence for Science connects scientific reasoning, experimentation, and discovery. Qatalyst makes that mission tangible through an inspectable loop: propose a method, implement it, execute a test, challenge the result, and revise. Today’s evidence concerns reconstruction of described quantum algorithms. The longer-term ambition is to help researchers explore new methods with explicit assumptions, reproducible artifacts, and tests strong enough to distinguish a plausible idea from a useful scientific contribution.

## What comes next—and where you can contribute

The next milestones are independent functional contracts, completed native and hybrid cohorts, budget-matched comparisons over repeated seeds, and clearer attribution of each model’s contribution. Beyond reconstruction, we want to investigate whether execution-guided search can propose useful algorithmic variations and whether domain tools can extend this workflow to other scientific questions. Those are research directions to test. Quantum scientists can sharpen correctness criteria; engineers can strengthen reproducibility; domain experts and curious newcomers can help define meaningful questions. Explore the source, inspect the evidence, and bring a problem worth testing.

## The people behind Qatalyst

Sanjay Das, Ethan Seefried, Chris, Tahisha, and Shaziaviedi developed this MIT Science Hackathon project. Their shared aim is to build scientific AI that makes its work visible and gives researchers a stronger starting point for the next experiment.

*Results snapshot: November 1, 2026, 11:21:52 a.m. EST. Based on the team-supplied algo-sim-REPORT.md. Native and hybrid batches are partial; reported readiness is execution plus agent review. The current evidence does not establish novel discovery, an evolutionary advantage, or full-paper reproduction.*
