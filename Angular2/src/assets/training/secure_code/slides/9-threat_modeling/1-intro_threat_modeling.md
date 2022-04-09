# 2. Threat Modeling

This chapter describes the basics of threat modeling along with a specific threat modeling approach called STRIDE.

Learning objectives:

1. Discuss the basics of threat modeling.

2. Explain what STRIDE is and its basic application.

## Threat Modeling/Attack Modeling

### Introduction to Threat Modeling

A useful trick for creating secure systems is to *think like an attacker* before you write the code or change to the code.

Threat modeling is the process of examining your requirements and design to consider how an attacker might exploit or break into your system, so that you can try to prevent those problems in the first place. For our purposes, we will consider the term *attack modeling* as a synonym with *threat modeling*, though some do use the terms to mean different things. Industry terminology differs a lot here, and we want to focus on what is useful to do, not what to call it. A great thing about threat modeling/attack modeling is that you can do this *before* a design is decided on or code is written, so they can help you very early when developing a new system.

If there is no meaningful security risk, threat modeling is probably unwarranted. Threat modeling is also probably not worth it if you are just writing a small component inside a system that is not focused on security (such as a single-function JavaScript package for doing simple text manipulation). Threat modeling generally focuses on larger systems where there are clear trust boundaries. But if there is a meaningful security risk, and you are building something larger, carefully thinking about things from the attacker’s point of view can be very useful.

There are many different ways to do threat modeling. For example, where do you start? Different approaches might emphasize starting with:

1. The attacker (what are the attacker’s goals? capabilities? way of doing things?)

2. The assets to be protected

3. The system design.

You should think at least a little about all of them, but it helps to have a place to start. Many security experts will start with the attacker or the assets. However, for many developers, it is often easiest to start with the design. Many developers don’t know how attackers operate in depth, and many organizations have a surprising amount of trouble figuring out what assets are most important. In contrast, if you develop software at all, then you *have* to be able to divide up a problem, so for most developers focusing on design starts with a natural strength. You should not *ignore* who the attacker is, or what assets need protecting; it is just a matter of emphasis.

A related problem is how to do this kind of analysis. Some people create a set of *attack trees*. Each tree identifies an event an attacker tries to cause, working backwards to show how the event could happen (hopefully, you will show that it cannot happen or is exceedingly unlikely). This approach can work well, but in practice, it requires expertise in attack methods; that is an expertise few developers have. Some approaches focus on analyzing an organization, but if your software will be used in many different organizations, then this does not work well.

For our purposes, we will focus in the next unit on a very simple approach called STRIDE.