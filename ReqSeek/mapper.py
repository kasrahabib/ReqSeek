def map(label):
    mapping = {
        'may_signal_keyword_requirement': 'requirement',
        'must_signal_keyword_requirement': 'requirement',
        'shall_signal_keyword_requirement': 'requirement',
        'should_signal_keyword_requirement': 'requirement',
        'will_signal_keyword_requirement': 'requirement',
        'may_signal_keyword_general_text': 'contextual_auxiliary',
        'must_signal_keyword_general_text': 'contextual_auxiliary',
        'no_signal_keyword_general_text': 'contextual_auxiliary',
        'shall_signal_keyword_general_text': 'contextual_auxiliary',
        'will_signal_keyword_general_text': 'contextual_auxiliary',
        'should_signal_keyword_general_text': 'contextual_auxiliary',
        'may_signal_keyword_srs_text': 'system_related_auxiliary',
        'must_signal_keyword_srs_text': 'system_related_auxiliary',
        'no_signal_keyword_srs_text': 'system_related_auxiliary',
        'shall_signal_keyword_srs_text': 'system_related_auxiliary',
        'should_signal_keyword_srs_text': 'system_related_auxiliary',
        'will_signal_keyword_srs_text': 'system_related_auxiliary',
            }
    return [mapping[i] for i in label]


def twoClassMapper(label):
    mapping = {
        'may_signal_keyword_requirement': 'requirement',
        'must_signal_keyword_requirement': 'requirement',
        'shall_signal_keyword_requirement': 'requirement',
        'should_signal_keyword_requirement': 'requirement',
        'will_signal_keyword_requirement': 'requirement',
        'may_signal_keyword_general_text': 'auxiliary',
        'must_signal_keyword_general_text': 'auxiliary',
        'no_signal_keyword_general_text': 'auxiliary',
        'shall_signal_keyword_general_text': 'auxiliary',
        'will_signal_keyword_general_text': 'auxiliary',
        'should_signal_keyword_general_text': 'auxiliary',
        'may_signal_keyword_srs_text': 'auxiliary',
        'must_signal_keyword_srs_text': 'auxiliary',
        'no_signal_keyword_srs_text': 'auxiliary',
        'shall_signal_keyword_srs_text': 'auxiliary',
        'should_signal_keyword_srs_text': 'auxiliary',
        'will_signal_keyword_srs_text': 'auxiliary',
            }
    return [mapping[i] for i in label]



def makeBinary(labels):
    two_class_label_mapper = {
        'may_signal_keyword_requirement': 'requirement_text', 'must_signal_keyword_requirement': 'requirement_text',
        'shall_signal_keyword_requirement': 'requirement_text', 'should_signal_keyword_requirement': 'requirement_text',
        'will_signal_keyword_requirement': 'requirement_text', 'may_signal_keyword_general_text': 'non_requirement_text',
        'must_signal_keyword_general_text': 'non_requirement_text', 'no_signal_keyword_general_text': 'non_requirement_text',
        'shall_signal_keyword_general_text': 'non_requirement_text', 'will_signal_keyword_general_text': 'non_requirement_text',
        'should_signal_keyword_general_text': 'non_requirement_text', 'may_signal_keyword_srs_text': 'non_requirement_text',
        'must_signal_keyword_srs_text': 'non_requirement_text', 'no_signal_keyword_srs_text': 'non_requirement_text',
        'shall_signal_keyword_srs_text': 'non_requirement_text', 'should_signal_keyword_srs_text': 'non_requirement_text',
        'will_signal_keyword_srs_text': 'non_requirement_text',}
    labels = [two_class_label_mapper[lbl] for lbl in labels]
    return labels

# Huggingface mappers:

def map_hf(label):
    mapping = {
        'may_signal_keyword_requirement': 'requirement',
        'must_signal_keyword_requirement': 'requirement',
        'shall_signal_keyword_requirement': 'requirement',
        'should_signal_keyword_requirement': 'requirement',
        'will_signal_keyword_requirement': 'requirement',
        'may_signal_keyword_general_text': 'contextual_auxiliary',
        'must_signal_keyword_general_text': 'contextual_auxiliary',
        'no_signal_keyword_general_text': 'contextual_auxiliary',
        'shall_signal_keyword_general_text': 'contextual_auxiliary',
        'will_signal_keyword_general_text': 'contextual_auxiliary',
        'should_signal_keyword_general_text': 'contextual_auxiliary',
        'may_signal_keyword_srs_text': 'system_related_auxiliary',
        'must_signal_keyword_srs_text': 'system_related_auxiliary',
        'no_signal_keyword_srs_text': 'system_related_auxiliary',
        'shall_signal_keyword_srs_text': 'system_related_auxiliary',
        'should_signal_keyword_srs_text': 'system_related_auxiliary',
        'will_signal_keyword_srs_text': 'system_related_auxiliary',
            }
    return mapping[label]



def twoClassMapper_hf(label):
    mapping = {
        'may_signal_keyword_requirement': 'requirement',
        'must_signal_keyword_requirement': 'requirement',
        'shall_signal_keyword_requirement': 'requirement',
        'should_signal_keyword_requirement': 'requirement',
        'will_signal_keyword_requirement': 'requirement',
        'may_signal_keyword_general_text': 'auxiliary',
        'must_signal_keyword_general_text': 'auxiliary',
        'no_signal_keyword_general_text': 'auxiliary',
        'shall_signal_keyword_general_text': 'auxiliary',
        'will_signal_keyword_general_text': 'auxiliary',
        'should_signal_keyword_general_text': 'auxiliary',
        'may_signal_keyword_srs_text': 'auxiliary',
        'must_signal_keyword_srs_text': 'auxiliary',
        'no_signal_keyword_srs_text': 'auxiliary',
        'shall_signal_keyword_srs_text': 'auxiliary',
        'should_signal_keyword_srs_text': 'auxiliary',
        'will_signal_keyword_srs_text': 'auxiliary',
            }
    return mapping[label]
