# Programming Labs

This repository contains programming labs and exercises on a variety of topics including, but not limited to:

- asychronous programming
- Python static type checking with mypy
- decorators and generators
- client-server architecture
- static code visualization (autogeneration of UML class diagrams from the source repository)
- dynamic code visualization (tracing, profiling, runtime analysis)
- refactoring / component replacement exercises
- monitoring and observability exercises
- software system failure modes
- distributed system design patterns

The unifying philosophy behind these labs is that they focus on the design, analysis, and maintenance of large-scale, real-time large scale software systems. 

The philosophy of these labs is a "learning by doing" approach with mind and hand. This is not a textbook to study, but rather a series of hands-on programming labs to do. We believe that standard programming textbooks are too theory and documentation-heavy and do not provide the engineer with enough hands-on intuition to actually "feel" how these systems work. Thus, minimal background reading will be provided, strictly the bare minimum necessary to complete the programming labs. The real learning will happen through writing, analyzing, and debugging code. 

Lastly, another benefit of this approach is that it prepares one to solve the actual, day-to-day problems faced by large technical organizations. It is one thing to grind algorithmic problems and memorize theory to get through an interview. It is completely another to practice working with real, hands-on systems and understand them intuitively. It is experience with the latter, rather than the former, that will set the practicing engineer up for success.

**A note on AI:** While we believe AI is a powerful tool, we ask that you refrain from using AI while you are solving the exercises for the best learning experience. 

# Setup
Although these labs can be completed on any machine, we recommend that you complete them on a Linux-based machine, since that is the standard OS for most production-grade environments. If your computer does not run Linux, you can rent a Linux box for as low as $3-4 dollars a month from a site such as [DigitalOcean](digitalocean.com) and SSH into it. Or, you can buy 

# Prerequisite knowledge
We will assume that you know the fundamentals of computer science and are familiar with basic Python programming. Additionally, familiarity with Linux, vim, tmux, and previous debugging and "hands-on building" experience are helpful but not required. If you lack some of the necessary prerequisites, don't worry. Just be prepared to put in some more work. All it takes is curiosity, patience, time, and effort.


# The Labs

Here are the labs: They are organized in the following dependency structure:
```
TODO
```

## Asyncio lab
This lab, located in the asyncio_lab folder, is designed to help programmers get familiar with the concepts such as IO wait, wasted CPU cycles, event loops, and loosely coupled, asynchronous microservices. We will also cover context managers and how they can be used with asychronous programs to create flexible, modular programs.

## Decorator lab
This lab is designed to teach users the basics of decorators. We will begin with a simple overview of what decorators are and use the decorator to time the performance of critical software components in a system. 

## Mypy lab
This lab is designed to get users familiar with how to use Mypy for type checking, and why it is important. We will include some real-world exercises where adding MyPy features allows the codebase to become more robust and maintainable.

## Generator / Coroutine lab
This is a lab getting users familiar with the underlying decorator / generator framework that Python uses. We will explore concepts such as the built in methods such as `__next__`, generator state, the coroutine paradigm, channels, and coroutine synchronization.

## Static code analysis lab
In this lab, you will learn how to use static code analysis tools like `pyreverse` and `pydeps` to analyze the class and module structure of large software repositories. You will then apply your newfound knowledge to a classic refactoring task--dependency inversion.

## Dynamic code analysis lab
In this lab, you will learn how to use dynamic code analysis tools like the sampling profiler `py-spy`, the call graph generator `pycallgraph`, and standard tracing tools like linux's `perf` and Gregg's flame graphs to analyze the runtime performance of a software system. We will use these tools to identify critical hot spots / performance bottlenecks and re-architect / refactor their components to improve their performance. 

## Metaprogramming lab (build your own tools!)
In this hands-on metaprogramming lab, you will explore how Python’s dynamic features empower you to write code that can inspect, modify, and generate other code—capabilities essential for understanding and managing large, complex codebases. Through practical exercises, you’ll use introspection tools like getattr(), dir(), and the inspect module to analyze the structure and behavior of Python programs at runtime, and experiment with decorators and metaclasses to dynamically alter classes and functions. You’ll learn to build custom tools that can characterize interfaces, components, and architectural layers within sprawling monorepos, even when documentation is lacking and code quality varies. By leveraging metaprogramming techniques, you’ll gain the skills to automate documentation, enforce design standards, and create bespoke analysis utilities. Most importantly, you will be able to use these techniques to build your own specialized tools that exceed the capabilities of standard off-the-shelf solutions, tailoring them precisely to the unique needs and challenges of your software systems. This lab is designed for advanced Python users seeking practical experience with powerful techniques that are crucial for maintaining and improving large-scale, real-world software systems.

## Multithreading / multiprocessing lab
This lab will cover multiprocessing and multithreading tasks for CPU-bound tasks, rather than IO-bound tasks. We will learn how to speed up some simple tasks and verify that the CPU utilization goes up as a result with standard Linux tools `top` and `ps -aux`. These include, but are not limited to, encryption, compression, and optimization.

## Code refactoring lab
In this lab, we will refactor a toy software system, the `Gazepointer` head tracking system, that has some design flaws. We will replace some of its older, more primitive components with more advanced components, while retaining backwards compatibility by keeping the interfaces the same, but improving performance and extensibility in the process.

## Real-time streaming lab I (simple streaming algorithms)
This lab covers the design and analysis of some canonical streaming algorithms, such as Bloom filter, FM algorithm, LSH, Maj-Maj, etc. We will design and build these algorithms from first-principles and understand how they work. We will then turn them into some simple production systems, and design and analyse their performance compared to more naive solutions and see how the performance, memory, and CPU utilization differ. 

## Real-time streaming lab II (encrypted streaming compression algorithms)
Now we will take our hard-earned knowledge in streaming lab I of fundamental streaming algorithms and use them to design an encrypted streaming data channel designed to send and receive data (any data) in real time. The data channel will first have a compression layer (incorporating streaming compression) and real-time encryption layer. We will use the canonical streaming algorithms we learned in streaming lab I as "hyperparameters" of the streaming channel, helping to optimize for maximum latency and throughout of the channel, similar to how channel gain and multipath fade / noise estimation parameters are used to optimize the fidelity of PHY RF channels.

## Real-time streaming lab III (voice streaming application)
In this final streaming lab, building off of labs I and II, we will apply the encrypted and compressed data channel that we have built to solve a tangible real-world problem: voice chat. We will adapt our real-time compression and encryption algorithms to voice data, taking into account the bursty and stochastic nature of voice chat and adapting our streaming algorithms (tuning their "hyperparameters") to provide the best quality of service.

## Network programming lab
This lab, we will answer the following question through learning by doing: what happens under the hood that enables two computers to communicate with each other? To do that we will be doing a deep dive down the whole protocol stack: HTTP, TCP, IP, Ethernet, MAC. Through it all, we will design our own primitive networking stack that enables this to happen, and compare our toy version with the real version through code review to understand how they work. After completing the lab, you should have a good understanding of what happens under the hood for popular networking operations like sending a `ping` request or executing `wget`. 

## Distributed systems lab I (metastable failure of microservice chain)
Here, we will design a simple chain (tree) of simple microservice echo servers, and analyze the emergent behaviors and failure modes of such a system. We will try to provide a rigorous theoretical account of the system dynamics of such a system, using principles from [Strogatz Nonlinear Dynamics and Chaos](https://www.biodyn.ro/course/literatura/Nonlinear_Dynamics_and_Chaos_2018_Steven_H._Strogatz.pdf), the [Metastable Failure Paper](https://sigops.org/s/conferences/hotos/2021/papers/hotos21-s11-bronson.pdf), and perhaps a bit of queueing theory. After rigorously deriving the failure dynamics of the system, we will induce actual failures "in the wild" to observe failure dynamics and build intuition. Such failure includes metastable overload, flooding (due to cycles), saturation, etc.

## Distributed systems lab II (key-value cache)
Now, we will extend the simple echo server into a real distributed key-value cache with nodes distributed across multiple "clients" and "servers". Again, we will try to derive theoretical system dynamics of such a system and verify it in practice by stress-testing the system to the limits, inducing failure modes, and collecting and plotting data (perhaps with streaming counters and awk-based logging) to verify that theory meets practice.

## Distributed systems lab III (consensus algorithm)
The final touch for our distributed system will be making the distributed key-value cache consistent and coherent. To do that, we will implement a consistency algorithm, such as Raft or Paxos, on top of the existing system. And then try to reason about its behavior and dynamics, and verify that our reasoning actually matches practice.

## Security lab
TODO need to think of stuff for this one. Common attack vectors, TLS, etc. Take an existing system and attack it / defend it