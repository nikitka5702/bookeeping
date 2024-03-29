import React, { Component } from 'react'
import { Formik, ErrorMessage } from 'formik'
import { Layout, Alert, Col, Row } from 'antd'
import { Form, Input, SubmitButton } from '@jbuschke/formik-antd'
import gql from 'graphql-tag'
import {Mutation} from 'react-apollo'
import * as Yup from 'yup'

const { Content } = Layout

const CREATE_USER = gql`
mutation CreateUser($username: String!, $email: String!, $password: String!) {
  createUser(username: $username, email: $email, password: $password) {
    user {
      id
    }
  }
}
`

const SignUpSchema = Yup.object().shape({
  username: Yup.string()
    .min(4, 'Too short')
    .max(50, 'Too long')
    .required('Required'),
  email: Yup.string()
    .email('Invalid email')
    .required('Required'),
  password: Yup.string()
    .required('Password required'),
  passwordConfirm: Yup.string()
    .oneOf([Yup.ref('password'),], 'Passwords must match')
    .required('Required')
})

export default class Register extends Component {
  render() {
    return (
      <Content
        style={{
          margin: '24px 16px',
          padding: 24,
          background: '#fff'
        }}
      >
        <Mutation
          mutation={CREATE_USER}
          update={(cache, {data: {createUser: {user: {id}}}}) => {
            this.props.history.push('/login')
          }}
          errors
        >
          {(createUser, { data, error }) => (
            <Formik
              initialValues={{username: '', email: '', password: '', passwordConfirm: ''}}
              validationSchema={SignUpSchema}
              onSubmit={(values, { setSubmitting }) => {
                const {username, email, password} = values
                setSubmitting(false)
                createUser({variables: {username, email, password}})
              }}
              render={({errors, status, touched, isSubmitting}) => (
                <Form>
                  <Row type="flex" justify="center" gutter={16}>
                    <Col span={6}>
                      <Form.Item>
                        <Input
                          name="username"
                          placeholder="Username"
                        />
                        <ErrorMessage name="username" />
                      </Form.Item>
                    </Col>
                    <Col span={6}>
                      <Form.Item>
                        <Input
                          name="email"
                          placeholder="Email"
                        />
                        <ErrorMessage name="email" />
                      </Form.Item>
                    </Col>
                  </Row>
                  <Row type="flex" justify="center" gutter={16}>
                    <Col span={6}>
                      <Form.Item>
                        <Input.Password
                          name="password"
                          placeholder="Password"
                        />
                        <ErrorMessage name="password" />
                      </Form.Item>
                    </Col>
                    <Col span={6}>
                      <Form.Item>
                        <Input.Password
                          name="passwordConfirm"
                          placeholder="Confirm Password"
                        />
                        <ErrorMessage name="passwordConfirm" />
                      </Form.Item>
                    </Col>
                  </Row>
                  <Row type="flex" justify="center">
                    <Col span={12}>
                      <SubmitButton>Register</SubmitButton>
                      <br/><br/>
                      {error ? error.graphQLErrors.map(({ message }, i) => <Alert key={i} message={message} type="error" />) : ''}
                    </Col>
                  </Row>
                </Form>
              )}
            />
          )}
        </Mutation>
      </Content>
    )
  }
}