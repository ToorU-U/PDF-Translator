# QA Checklist

This checklist defines the minimum quality gates before exporting or accepting a translated DOCX.

## Editable Text Checks

- [ ] The DOCX contains real editable text.
- [ ] Editable text character count is above the configured threshold.
- [ ] Body text can be selected.
- [ ] Body text can be copied.
- [ ] Body text can be searched.
- [ ] Body text can be edited.

## Paragraph and Heading Checks

- [ ] Paragraph count is reasonable for the source document.
- [ ] Major sections use Word Heading styles.
- [ ] Subsections use appropriate lower-level Heading styles.
- [ ] Numbering is preserved.
- [ ] Units are preserved.
- [ ] Terminal numbers and wire labels are preserved.

## Table Checks

- [ ] Table count is reasonable for the source document.
- [ ] Tables are Word tables where feasible.
- [ ] Rows and columns are in the correct order.
- [ ] Header rows are preserved where feasible.
- [ ] Cell text is editable.

## Image Checks

- [ ] Images are independent Word image objects.
- [ ] Images are not full-page substitutes for document pages.
- [ ] Images can be selected and moved in Word.
- [ ] Image count is reasonable for the source document.
- [ ] Image resolution is preserved as much as possible.
- [ ] Images with Chinese labels are exported to `images_to_translate/`.
- [ ] `image_mapping.json` includes every image requiring translation.

## Full-Page Image Failure Detection

Fail the output if:

- [ ] Editable text is near zero.
- [ ] The number of large page-sized images is close to the page count.
- [ ] Most pages consist of one large image.
- [ ] Paragraph count is too low for the source.

## Chinese Residual Checks

- [ ] Editable body text contains no untranslated Chinese.
- [ ] Headers and footers contain no untranslated Chinese.
- [ ] Table cells contain no untranslated Chinese.
- [ ] Captions contain no untranslated Chinese.
- [ ] Any Chinese remaining inside images is listed in `image_mapping.json` for separate image translation.

## Image Mapping Checks

- [ ] `image_mapping.json` exists.
- [ ] Every image has a unique `image_id`.
- [ ] Every mapped image file exists.
- [ ] Source page number is recorded.
- [ ] Insert-back location is recorded.
- [ ] Original image size is recorded.
- [ ] Expected translated image path is recorded.

## Report Checks

- [ ] `translation_report.md` exists.
- [ ] Report includes source summary.
- [ ] Report includes text extraction counts.
- [ ] Report includes table counts.
- [ ] Report includes image counts.
- [ ] Report includes QA pass/fail status.
- [ ] Report lists missing translated images, if any.

## Final Gate

The document may be accepted only if:

- [ ] QA status is PASS.
- [ ] No full-page image failure pattern is detected.
- [ ] The DOCX is editable.
- [ ] Required output files exist.

