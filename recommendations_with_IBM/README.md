### Concepts in Experiment Design

#### Types of Study
- If you have a lot of control over features, then you have an **experiment**.
- If you have no control over the features, then you have an **observational** study.
- If you have some control, then you have a **quasi-experiment**.

examples:

Observational Study , Historic data is collected to compare the effect of local curfew ordinances and downtown foot traffic.

Experiment, An online retailer sends out personal coupon codes to half of their mailing list.

Quasi-Experiment , A blogger tries out a celebrity diet and exercise regimen and documents their changes in weight and energy.

#### Types of Experiment
- between-subjects experiment.
- within-subjects experiment.

**control group** , either no manipulation or maintenance of the status quo.
**experimental group** , it includes the manipulation we wish to test.

**A/B test** : one control group A, one experimental group B.

**A/B/C test** : one control group A, two experimental group B & C.

examples:

between-subject experiment , Testing a new drug where half of the subjects are provided with the new drug and the other half are given a placebo.

within-subject experiment , Asking restaurant patrons to try three different recipes of a single dish, providing feedback on each one.

#### SMART Mnemonic for Experiment Design
There's a mnemonic called SMART for teams to plan out projects that also happens to apply pretty well for creating experiments. The letters of SMART stand for:
- Specific: Make sure the goals of your experiment are specific.
- Measurable: Outcomes must be measurable using objective metrics.
- Achievable: The steps taken for the experiment and the goals must be realistic.
- Relevant: The experiment needs to have a purpose behind it.
- Timely: Results must be obtainable in a reasonable time frame.

#### Types of Sampling
- Simple random sampling , all members of the population have equal chance of selection.
- Stratified random sampling , divide population into distinct subgroups, then sample from each group.

**Evaluation** metrics were mentioned on the previous page as the metrics by which we compare groups. Ideally, we hope to see a difference between groups that will tell us if our manipulation was a success. 

Evaluation metrics , There is at least one feature difference between groups.

Invariant metrics , There are no feature differences between groups.

Confounding variables , The correlation observed between two variables might be due to changes in a third variable, rather than one causing the other. 

**In order to determine causality between two features, following are important steps to take**
- manipulate only one of the features.
- ensure all other features (other than the one being tested) are not manipulated.

**The situations involving confounding variables**
- There is a correlation observed between two variables that might be due to changes in a third variable, rather than one causing the other.
- There is a causal relationship between the two features, but it is an indirect relationship mediated by a third, intermediate variable.

#### Checking Validity

When designing an experiment, it's important to keep in mind validity, which concerns how well conclusions can be supported. There are three major conceptual dimensions upon which validity can be assessed:
- Construct Validity , How well one's goals are aligned to the evaluation metrics used to evaluate it.
- Internal Validity , Refers to the degree to which a causal relationship can be derived from an experiment's results.
- External Validity , Concerned with the ability of an experimental outcome to be generalized to a broader population.

#### Checking Bias

Biases in experiments are systematic effects that interfere with the interpretation of experimental results, mostly in terms of internal validity.

- Sampling bias , Occurs when some members of a population are more likely to be selected in a sample than others.
- Novelty bias , Occurs when the mere appearance of a new treatment makes it seem better.
- Order bias , Occurs when respondents are influenced to select specific responses based simply because of the order they are shown.
- Experimenter bias , Occurs when a researcher unconsciously affects the actions or results of an experiment

#### Ethical principles in experiment design
- minimize participant risk
- clear benefits of risks taken
- provide informed consent
- handle sensitive data appropriately


#### Glossary

KeyTerm , Definition
- **A/B test** , A web-based experiment where the outcomes between groups (e.g. recovery time or click-through rate) are compared in order to make a judgment about the effect of our manipulation.
- **Between-subjects experiment** , Each unit only participates in, or sees, one of the conditions being used in the experiment.
- **Blinding** , The administrator of a procedure or the participant does not know the condition being used, to avoid that subconscious bias from having an effect.
- **Confounding variables** , When we aren't able to control all features or there is a lack of equivalence between groups.
- **Construct validity** , How well one's goals are aligned to the evaluation metrics used to evaluate it.
- **Control group** , No manipulation or maintenance of the status quo.
- **Convenience sample** , Records information from readily available units.
- **Double-blind** , Hides condition information from both the administrator and participant in order to have a strong rein on experimenter-based biases.
- **Evaluation metrics** ,	The objective features by which you evaluate performance or the metrics by which we compare groups.
- **Experimental group** , Manipulation we wish to test, such as a new drug or new website layout.
- **Experimenter bias**	, Where the presence or knowledge of the experimenter can affect participants' behaviors or performance.
- **External validity** , The ability of an experimental outcome to be generalized to a broader population.
- **Factorial designs** , Manipulate the value of multiple features of interest
- **Internal validity** , The degree to which a causal relationship can be derived from an experiment's results.
- **Invariant metrics** , metrics that we hope will not be different between groups
- **Non-proportional sample** , Samples taken are not proportional to the overall size of the group in the population and requires weighting each group separately
- **Novelty bias** , When observers change their behavior simply because they're seeing something new.
- **Order bias** , In a within-subject experiment, when the order in which conditions are completed could have an effect on participant responses.
- **Primacy effect** , One that affects early conditions, perhaps biasing them to be recalled better or to serve as anchor values for later conditions.
- **Proportional sample** ,	The sample size is proportional to how large the group is in the full population.
- **Recency effect** , One that affects later conditions, perhaps causing bias due to being fresher in memory or task fatigue.
- **Repeated measures experiment** , Another name for a within-subject experiment
- **Sampling bias** , Those biases that cause our observations to not be representative of the population.
- **Self-selection bias** , The types of people that respond to a survey might be qualitatively very different from those that do not.
- **Simple random sampling** , Each individual in the population has an equal chance of being selected
- **Stratified random sampling** , The entire population is first divided into disjoint groups or strata. Each individual must be a part of one group and only one group.
- **Survivor bias** , When losses or dropout of observed units is not accounted for in an analysis.
- **Unit of Analysis** , The entity under study
- **Within-subjects experiment** , When an individual completes all conditions, rather than just one.

------------------------------------------------------
### Statistical Considerations in Testing

