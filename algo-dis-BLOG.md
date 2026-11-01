# Algorithm Discovery for Science: turning ideas into testable experiments

From research abstracts to executable experiments: Qatalyst explores how cooperating AI agents can support a transparent, testable path toward autonomous discovery.

**MIT Science Hackathon project · Qatalyst**  
**Team:** Sanjay Das, Ethan Seefried, Chris, Tahisha, Shaziaviedi

## From a scientific idea to an experiment

A research abstract can describe a powerful idea in a few paragraphs. Turning that idea into equations, working software, and a convincing experiment can take much longer. What if AI agents could help researchers cross that gap—and leave a clear record of every proposal, test, and revision? Algorithm Discovery for Science explores that question. Our MIT Science Hackathon prototype, Qatalyst, starts with quantum-algorithm abstracts and attempts to reconstruct executable methods from their descriptions.

## A small research team, expressed in software

Imagine a research team with a shared notebook: one colleague proposes a method, another turns it into code, and a reviewer asks whether the evidence supports the claim. Qatalyst organizes three cooperating AI agents around a shared task board. Two can develop implementations, while a third stays outside implementation chains to provide independent review. The agents have a virtual energy budget; when one exhausts it, a replacement can inherit a successful strategy with a small variation or try a fresh approach. The lobster-themed agents give this experimental workflow its personality.

## Inside the discovery loop

A locally hosted, fine-tuned Nemotron model proposes numbered equations in LaTeX. Sonnet plans methods, assembles specifications, writes Qiskit code, and reviews results. Generated code builds in an isolated Docker worker, and Qiskit Aer simulates the quantum circuits. The agents operate on one host and share model services. In plain language, the workflow moves from an idea to a mathematical proposal, then to code, a simulated experiment, criticism, and revision. Each stage creates evidence that a researcher can inspect.

## An encouraging reconstruction—with a precise scope

One supplied abstract concerned an affine Boolean function, f(x) = a·x ⊕ b: a simple rule with a hidden bit string a and an offset b. The task was to recover both. The swarm selected a circuit combining an offset readout with a Bernstein–Vazirani step. For n = 2, a = 1, and b = 1, Aer returned 101 in all 1,024 shots, encoding the expected hidden values. Separate small-instance checks recovered both values in 28 of 28 cases across one to three data qubits. The recorded swarm run took about 4.4 minutes, with estimated paid usage of $0.31.

## What that result establishes

These checks support a limited reconstruction result under the implemented assumptions. The circuit compiles explicit oracle parameters into gates and assumes controlled-phase-oracle access. It does not establish the source paper’s black-box query complexity or its claims about incompletely defined functions. Attribution also matters: Sonnet rejected all eight native equation proposals and assembled the successful specification itself. Understanding which component contributed to a result is essential to improving the system.

## A useful failure is part of the science

A second abstract concerned order finding with imperfect gates. The swarm generated a small N = 15 circuit that built and simulated, but the default-zero-input run concentrated on 00000000. Review requested alignment of the work-register initialization across the specification, circuit, and runner. The system attempted repairs, recorded two agent deaths and two replacements, and reached its time limit without an approved candidate. The reviewer’s objection was not independently confirmed as a numerical counterexample, so the outcome remains unresolved. This case exposes a concrete verification task: successful execution alone cannot establish scientific correctness.

## Why this belongs in autonomous science

SI²’s mission connects scientific reasoning, experimentation, and discovery. Algorithm Discovery for Science puts that connection into a testable workflow: translate a research goal into a candidate method, execute it, examine the evidence, and revise the next step. The current prototype studies reconstruction of described algorithms; original algorithm discovery remains a longer-term research goal. Preserved proposals, code, feedback, and strategy lineage make the process inspectable, while human researchers define the questions, evaluate assumptions, and decide what the results justify.

## The next questions are an invitation

Our next priorities are independent functional checks, clearer separation of reconstruction from novelty, and evaluations that identify which parts of the agent workflow improve outcomes. A stronger system should explain why a candidate works, when it fails, and what evidence would change its conclusion. Quantum researchers can help sharpen the tests; software engineers can strengthen reproducibility; researchers across disciplines can bring problems with clear success criteria. If you are curious about how an idea becomes an experiment, there is a place for your perspective in this work. Explore the project and connect with SI² to help shape the next questions.

[Explore Algorithm Discovery for Science](https://si2research.github.io/projects/algorithm-discovery-for-science/) · [Autonomous Labs](https://si2research.github.io/research/autonomous/)

*Research note: Experimental details are drawn from the team-supplied Qatalyst draft. These are prototype observations, not a claim of novel algorithm discovery or a peer-reviewed evaluation.*
