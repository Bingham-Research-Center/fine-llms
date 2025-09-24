# Paper Prioritization and Data Prep Guide

This document provides a prioritized list of the papers discussed in the research summary, as well as guidance on how to prepare your data for fine-tuning.

## Paper Prioritization

To help you focus your data creation efforts, here is a list of the papers from the research summary, ranked by their frequency of citation in the main text. This can be used as a proxy for their importance in the context of this research summary.

### High Priority (Cited 5+ times)

*   **Lyman and Tran, 2015:** (Meteorology, Organic Compounds)
*   **Mansfield and Hall, 2018:** (Meteorology)
*   **Edwards et al., 2014:** (Ambient Air Chemistry, Organic Compounds)
*   **Koss et al., 2015:** (Ambient Air Chemistry, Organic Compounds)

### Medium Priority (Cited 3-4 times)

*   **Schnell et al., 2016:** (Meteorology, Reactive Nitrogen)
*   **Tran et al., 2018:** (Computer Simulations)
*   **Ahmadov et al., 2015:** (Computer Simulations)
*   **Matichuk et al., 2017:** (Computer Simulations)
*   **Wild et al., 2016:** (Reactive Nitrogen)

### Standard Priority (Cited 1-2 times)

*   (A complete list of all papers is in the `PAPERS-TO-PRECIS.md` file)

**Recommendation:** Start by creating detailed summaries and Q&A pairs for the papers in the "High Priority" and "Medium Priority" categories. This will give your model a strong foundation in the most important concepts.

## Q&A Template (Markdown)

Here is a "pretty" Markdown template that you can use to create your Q&A pairs. You can then easily convert this to JSONL format later.

---

**Question:** What are the three key ingredients for winter ozone formation in the Uinta Basin?

**Answer:** Significant local ozone production during wintertime requires three ingredients: thermal inversions, snow cover, and precursor emissions from the oil and gas industry.

**Source:** (Lyman and Tran, 2015; Mansfield, 2017; Mansfield and Hall, 2013; Mansfield and Hall, 2018; Oltmans et al., 2014; Schnell et al., 2009)

---

**Question:** Why is snow cover important for winter ozone formation?

**Answer:** The snow surface reflects rather than absorbs solar radiation, the energy source for ozone formation. This increases the amount of radiation available in the atmosphere for chemical reactions. Snow cover also acts to stabilize inversions by reflecting sunlight and keeping the surface cool.

**Source:** (Lyman and Tran, 2015; Mansfield, 2017; Mansfield and Hall, 2013; Mansfield and Hall, 2018; Oltmans et al., 2014; Schnell et al., 2009)

---

## Text-Tuning Techniques

Here are some simple techniques you can use to "tune" your existing text to make it more suitable for fine-tuning:

*   **Simplify Sentences:** Break down long, complex sentences into shorter, simpler ones.
*   **Define Jargon:** If you must use jargon, make sure it is clearly defined in the text.
*   **Use Active Voice:** Use active voice instead of passive voice to make the text more direct and easier to understand.
*   **Remove Redundancy:** Remove any redundant information or repetitive phrasing.
*   **Add Context:** Add context to ambiguous statements to make them clearer.

By applying these simple techniques, you can significantly improve the quality of your training data without having to do a lot of extra writing.
