#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#[aws-lambda-autoscale-adjust-size.py]
#
#Copyright (c) 2015 Masaru Kawabata
#
#This software is released under the MIT License.
#http://opensource.org/licenses/mit-license.php

"""
[概要]
 - AWS-Lambda AutoScalingGroupの台数調整

[機能]
 - AWS-LambdaのCron機能を利用して、AutoScalingGroupの起動台数を調整する
"""

__authour__ = "masaru.kawabata"
__version__ = 0.1

import boto3

def minsizeXXX(event, context):
    """
    AutoScalingGroup起動台数調整
    """

    """ Create Connection """
    try:
        client = boto3.client('autoscaling', region_name = '<Region>')
    except:
        print('Connection Error')
        return 1

    """ Update AutoScalingGroup """
    try:
        client.update_auto_scaling_group(AutoScalingGroupName = '<AutoScalingGroup>', MinSize = XXX, DesiredCapacity = XXX)
    except: 
        print('Update AutoScalingGroup Error')
        return 1

    return 0

def minsizeYYY(event, context):
    """
    AutoScalingGroup起動台数調整
    """

    """ Create Connection """
    try:
        client = boto3.client('autoscaling', region_name = '<Region>')
    except:
        print('Connection Error')
        return 1

    """ Update AutoScalingGroup """
    try:
        client.update_auto_scaling_group(AutoScalingGroupName = 'jl-pro-group-spot', MinSize = YYY, DesiredCapacity = YYY)
    except: 
        print('Update AutoScalingGroup Error')
        return 1

    return 0

