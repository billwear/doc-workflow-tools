#!/usr/bin/python3

import json, subprocess, errno

def md_api_get_topic(topic_id, credentials):
    '''
    gets topic_id from the Discourse server indicated in the credentials; 
    handles Discourse API wait requests and other transient errors, 
    in case a large number of calls are made in a short time period
    '''

    # set rate limit error flag to True
    rate_limit_error = True

    # while rate limit error is True
    while rate_limit_error == True:

        ## do the curl call
        proc = subprocess.Popen(
            [
                "curl",
                "-s",
                "-X",
                "GET",
                "-H",
                "Api-Key: " + credentials["api_key"],
                "-H",
                "Api-Username: " + credentials["api_username"],
                "-H",
                "Content-Type: application/json",
                credentials["base_url"] + "/t/{" + str(topic_id) + "}.json",
            ],
            stdout=subprocess.PIPE,
        )

        ## read the curl result into a usable buffer
        output = proc.stdout.read()

        ## try to convert the result to json
        try:
            topic_json = json.loads(output)
        except:
            ### handle "topic doesn't exist" error
            return(errno.ENODATA, "Topic doesn't exist")

        ## try to see if there's a rate_limit error
        try:
            ### if so, sleep for 20s and continue the loop
            if topic_json["error_type"] == "rate_limit":
                rate_limit_error = True
                time.sleep(20)
                continue;
        except:
            return(0, topic_json)
    
def md_api_put_topic(topic_id, credentials):
    '''
    puts a new version of topic_id to the Discourse server indicated in 
    the credentials; handles Discourse API wait requests and other transient 
    errors, in case a large number of calls are made in a short time period.
    '''

    return(error_code, call_status)
    
def md_api_get_latest_revision(topic_id, credentials):
    '''
    gets latest revision for topic_id from the Discourse server indicated in 
    the credentials; handles Discourse API wait requests and other transient 
    errors, in case a large number of calls are made in a short time period.
    '''

    return(error_code, latest_revision_json)

def md_api_get_post(post_id, credentials):
    '''
    gets post_id from the Discourse server indicated in the credentials; 
    handles Discourse API wait requests and other transient errors, in case a 
    large number of calls are made in a short time period.
    '''

    return(error_code, post_json)

def md_api_put_post(post_id, credentials):
    '''
    puts a new version of topic_id the Discourse server indicated in the credentials; 
    handles Discourse API wait requests and other transient errors, in case a large 
    number of calls are made in a short time period.
    '''

    return(error_code)

def md_api_has_been_updated(topic_id, interval, credentials):
    '''
    checks to see whether a topic has been updated in the last interval hours
    '''

    return(was_updated)

def md_set_credentials(credential_file_path):
    '''
    reads API URL and credentials from a specified file into a list for use with
    the various API calls above
    '''

    return(error_code)

def md_get_last_edit_timestamp(revision_json):
    '''
    pulls the last edited timestamp from the passed JSON dictionary containing 
    information about the latest revision of a topic.
    '''

    return(error_code, le_timestamp)
    
def md_get_last_editor_username(revision_json):
    '''
    pulls the username of the user who last edited a topic from the passed JSON 
    dictionary containing information about the latest revision of a topic.
    '''

    return(error_code, le_username)
    
def md_get_post_number(topic_json):
    '''
    pulls the post number for the first post in a topic (needed for most topic 
    modifications) from the passed JSON dictionary containing information about 
    a topic.
    '''

    return(error_code, post_number)

def md_get_markdown_content(post_json):
    '''
    pulls the actual topic markdown content from the passed JSON dictionary 
    containing information about a post.
    '''

    return(error_code, markdown)

def md_is_later_than(timestamp_1, timestamp_2):
    '''
    compares two Discourse timestamps as strings and returns True if the second 
    passed timestamp is later than the first.  Discourse timestamps in JSON payloads 
    are formatted as strings in a way that does not require converting them to 
    datetime types to compare them.
    '''

    return(error_code, is_later_than)

def md_is_earlier_than(timestamp_1, timestamp_2):
    '''
    compares two Discourse timestamps as strings and returns True if the second 
    passed timestamp is earlier than the first.
    '''

    return(error_code, is_earlier_than)

def md_is_identical_to(timestamp_1, timestamp_2):
    '''
    compares to Discourse timestamps as strings and returns True if they 
    are identical.
    '''

    return(error_code, is_identical_to)
