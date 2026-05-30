# Can Clinical Cognition Be Reconstructed?

Positioning: methodology paper for the Clinical Cognition Transformation Lab (CCTL).

## Abstract

Clinical decisions often leave behind artifacts: referral letters, consultation notes, treatment plans, longitudinal records, AI-generated summaries, and other forms of clinical documentation. These artifacts rarely preserve the full reasoning event that produced them. They may compress uncertainty, omit alternatives, translate specialist judgment, introduce new interpretations, or convert provisional thinking into operational action. Yet they may still contain traces of clinical cognition.

This paper proposes Cognitive Reconstruction as a method for studying whether clinical cognition can be partially reconstructed from downstream artifacts after the original reasoning event has disappeared. The goal is not to recover a perfect copy of prior thought. Rather, the goal is to infer which elements of cognition were preserved, transformed, delegated, lost, or newly introduced as clinical meaning moved across people, documents, AI systems, workflows, and institutions. The paper defines artifact pair analysis, reconstruction layers, sources of drift, failure modes, and evaluation criteria for empirical study.

## Problem Statement

Much clinical cognition is transient. A clinician notices a subtle pattern, weighs alternatives, decides that one finding is more important than another, considers a patient's constraints, or holds uncertainty that never fully enters the chart. Later, only artifacts remain.

Those artifacts are often treated as records of clinical work. They are also transformations of clinical work. A referral letter is not the same as the reasoning that led to referral. A specialist consultation note is not the same as the specialist's full interpretive process. An AI-generated summary is not the same as the source record it condenses. A treatment plan is not the same as the cognitive pathway that made the plan reasonable.

CCTL's methodological question is whether these downstream artifacts can be studied as partial traces of distributed clinical cognition. How much cognition survives? What changes? What disappears? What is added later? What can researchers responsibly infer, and where must they stop?

## Clinical Cognition as Trace

Clinical cognition may survive as traces embedded within artifacts. These traces may include diagnostic labels, causal claims, uncertainty markers, evidence selections, temporal sequences, treatment intent, exclusions, risk assessments, patient preferences, and references to prior reasoning.

Traces are not transparent windows into cognition. They are partial, situated, and shaped by documentation norms, institutional templates, time pressure, specialty language, billing requirements, AI mediation, and audience. A trace may preserve one part of cognition while distorting another. It may signal a reasoning pathway without fully documenting it.

The premise of Cognitive Reconstruction is therefore cautious: artifacts may not reproduce original cognition, but they may allow partial reconstruction. The method studies what can be inferred, how confident the inference should be, and which parts of the original cognitive event remain unrecoverable.

## Why Reconstruction Matters

Cognitive Reconstruction matters because distributed clinical systems depend on inherited cognition. Downstream clinicians, AI systems, institutions, patients, and caregivers often act on artifacts produced by earlier reasoning events. If those artifacts preserve only conclusions, later actors may lose access to uncertainty, alternatives, rationale, and responsibility.

Reconstruction also matters for research. If clinical cognition is increasingly distributed, researchers need methods for studying cognition outside direct observation. Real clinical workflows leave artifact trails. Those trails can be used to study preservation, compression, delegation, reframing, recommendation drift, and documentation-mediated transformation.

Finally, reconstruction matters for accountability. When an outcome is questioned, investigators may need to know not only what decision was made, but how the cognitive pathway evolved across handoffs, notes, AI systems, and treatment plans.

## Downstream Artifacts

Downstream artifacts are clinical materials that appear after an initial reasoning event and carry some transformed version of that cognition forward. They include:

- referral letters;
- specialist consultation notes;
- primary assessments;
- final treatment plans;
- clinical documentation;
- longitudinal records;
- AI-generated summaries;
- AI interpretations;
- patient-facing explanations;
- care coordination messages.

Each artifact has a purpose and audience. Referral letters may foreground why specialist input is needed. Consultation notes may reorganize the case around a specialist frame. Treatment plans may prioritize action over diagnostic nuance. AI summaries may condense large records into salient claims. Patient-facing explanations may translate uncertainty into usable language.

The reconstruction method must account for these purposes rather than treating every artifact as a neutral container of facts.

## Artifact Pair Analysis

Artifact pair analysis compares an upstream artifact with a downstream artifact to study how cognition changes across a transition.

Suggested artifact pairs include:

- Referral Letter <-> Specialist Consultation Note;
- Primary Assessment <-> Final Treatment Plan;
- Clinical Documentation <-> AI Interpretation;
- Human Assessment <-> AI Summary.

For each pair, researchers ask what clinical claims, evidence, uncertainties, mechanisms, priorities, and responsibilities appear in the source artifact and how they are preserved, transformed, delegated, omitted, or newly introduced in the downstream artifact.

The point is not merely to compare text. The point is to compare cognitive structure: what the case is understood to be, what evidence is treated as important, what uncertainty remains visible, what action is implied, and who or what appears responsible for the next step.

## Reconstruction Framework

Cognitive Reconstruction begins with three inputs: a source artifact, a downstream artifact, and contextual metadata. The source artifact may be a referral letter, primary assessment, human interpretation, or earlier clinical note. The downstream artifact may be a consultation note, treatment plan, AI summary, patient-facing explanation, or later record. Contextual metadata may include time interval, role, specialty, workflow stage, AI involvement, intended audience, and known constraints.

The analysis then proceeds through inference layers:

- preserved cognition: reasoning elements that remain traceable across artifacts;
- transformed cognition: reasoning elements that change form, emphasis, scope, or meaning;
- delegated cognition: cognitive work assigned to an AI system, specialist, workflow, or downstream actor;
- missing cognition: reasoning that appears necessary but is absent or unrecoverable;
- newly introduced cognition: claims, interpretations, uncertainties, or recommendations that appear downstream without a clear upstream source.

The outputs are a reconstruction hypothesis, an uncertainty assessment, and a drift characterization. A reconstruction hypothesis states what prior cognition most likely produced or contributed to the downstream artifact. An uncertainty assessment states the confidence and limits of that inference. A drift characterization describes how cognition changed across the transition.

## Sources of Drift

Drift occurs when clinical cognition changes across artifact transitions. Some drift is expected and appropriate. A specialist may legitimately reframe a case. A treatment plan may appropriately simplify reasoning for action. An AI summary may highlight different evidence because its task is different from the clinician's original task.

Sources of drift include:

- audience shift, such as clinician-to-specialist or clinician-to-patient communication;
- specialty reframing;
- documentation templates;
- time pressure;
- billing or administrative requirements;
- AI summarization or recommendation;
- uncertainty compression;
- selective evidence transfer;
- institutional protocol;
- patient preference or constraint;
- new information introduced between artifacts.

The method should distinguish harmful drift from necessary transformation. Not every change is an error.

## Failure Modes

Cognitive Reconstruction can fail in several ways.

First, artifacts may be too sparse. A referral letter that contains only a diagnosis and request may not preserve enough reasoning to reconstruct the upstream cognitive pathway.

Second, artifacts may be retrospectively rationalized. A note may describe a clean reasoning path that was assembled after the decision rather than during it.

Third, documentation may preserve institutional requirements more than clinical cognition. Templates may create apparent reasoning structure where little was actually recorded.

Fourth, AI-generated artifacts may sound coherent while obscuring their source selection, ranking, or omission logic.

Fifth, multiple plausible reconstructions may fit the same artifacts. In such cases, the method should preserve uncertainty rather than forcing a single narrative.

Failure is not useless. It identifies where cognition is not recoverable and where documentation, provenance, or workflow design may need improvement.

## Evaluation Criteria

Reconstruction quality should be evaluated across multiple dimensions.

- Fidelity: how well the reconstruction matches available evidence.
- Uncertainty preservation: whether the reconstruction preserves uncertainty rather than overstating confidence.
- Causal reasoning preservation: whether mechanisms and rationales remain traceable.
- Treatment intent preservation: whether the intended purpose of action is preserved.
- Missing assumptions: whether unstated assumptions are identified.
- Newly introduced reasoning: whether downstream additions are distinguished from upstream cognition.
- Drift severity: whether the transformation changes clinical meaning, responsibility, or action.

These criteria should be applied cautiously. The goal is not to prove that the original cognition is fully known. The goal is to make the limits of reconstruction explicit.

## Pilot Study Proposal

An initial pilot study could examine referral letters and specialist consultation notes. The study would collect paired artifacts from a defined clinical workflow, remove identifying information, and annotate each pair for preserved claims, transformed claims, uncertainty markers, missing rationale, newly introduced interpretations, and recommended actions.

Researchers would generate reconstruction hypotheses from referral letters alone, then compare them with specialist consultation notes. A second analysis would examine how the specialist note reframed or reconstructed the referral cognition. If AI-generated summaries are available, the study could compare human-to-human transitions with AI-mediated transitions.

Minimal outcomes would include reconstruction fidelity, uncertainty preservation, drift types, and common failure modes. The pilot would not claim to recover original cognition completely. It would test whether artifact pairs can support disciplined partial reconstruction.

## Discussion

Cognitive Reconstruction is a method for studying clinical cognition after the original reasoning event has disappeared. It treats documentation not merely as administrative residue, but as a trace-bearing medium through which cognition moves and changes.

The method is intentionally modest. It does not assume that all cognition can be recovered, that documentation is neutral, or that downstream artifacts are reliable mirrors of prior thought. It instead asks what can be inferred responsibly from artifacts, how uncertainty should be represented, and where cognition becomes unrecoverable.

This approach connects CCTL's broader research agenda to empirical study. Paper 1 argues that clinical cognition is becoming distributed. Paper 2 proposes that AI-mediated expertise change should be studied as transformation rather than presumed decay. This paper proposes a method for observing some of those transformations through artifact trails.

## Conclusion

Clinical cognition may survive as traces embedded within artifacts. These traces may not perfectly reproduce original cognition, but they may allow partial reconstruction.

Cognitive Reconstruction offers a cautious methodology for studying how clinical meaning, uncertainty, responsibility, and intent change across referral letters, consultation notes, treatment plans, longitudinal records, AI-generated summaries, and clinical documentation. Its central contribution is not certainty. Its contribution is a structured way to ask what cognition survived, what transformed, what was delegated, what went missing, and what was newly introduced.

For CCTL, this method provides one path from conceptual manifesto to empirical research on Human-AI Clinical Cognition.
