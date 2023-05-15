import { IRegister, convertBase64, register } from "@/lib/api"
import { useState } from "react"

export default function Register() {
  const [data, setData] = useState<IRegister>({
    name: "",
    email: "",
    password: "",
    billing_address: "",
    shipping_address: "",
    payment_methods: "",
    image: ""
  })

  const handleSubmit = (e: any) => {
    e.preventDefault()

    register(data).then((res) => {
      console.log(res)
    })
  }

  const handleImageUpload = async (e: any) => {
    const file = e.target.files[0]
    const base64 = await convertBase64(file)
    setData({ ...data, image: base64 })
  }

  return (
    <div className="h-screen w-screen">
      <div className="min-h-full flex">
        <div className="flex-1 flex flex-col justify-center py-12 px-4 sm:px-6 lg:flex-none lg:px-20 xl:px-24">
          <div className="mx-auto w-full max-w-sm lg:w-96">
            <div>
              <img
                className="h-12 w-auto"
                src="https://tailwindui.com/img/logos/workflow-mark-indigo-600.svg"
                alt="Workflow"
              />
              <h2 className="mt-6 text-3xl font-extrabold text-gray-900">Create your account</h2>
            </div>

            <div className="mt-8">
              <div className="mt-6">
                <form action="#" method="POST" className="space-y-6">
                  <div>
                    <label htmlFor="name" className="block text-sm font-medium text-gray-700">
                      Name
                    </label>
                    <div className="mt-1">
                      <input
                        id="name"
                        name="name"
                        type="name"
                        autoComplete="name"
                        required
                        className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                        value={data.name}
                        onChange={(e) => setData({ ...data, name: e.target.value })}
                      />
                    </div>
                  </div>
                  <div>
                    <label htmlFor="email" className="block text-sm font-medium text-gray-700">
                      Email address
                    </label>
                    <div className="mt-1">
                      <input
                        id="email"
                        name="email"
                        type="email"
                        autoComplete="email"
                        required
                        className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                        value={data.email}
                        onChange={(e) => setData({ ...data, email: e.target.value })}
                      />
                    </div>
                  </div>

                  <div className="space-y-1">
                    <label htmlFor="password" className="block text-sm font-medium text-gray-700">
                      Password
                    </label>
                    <div className="mt-1">
                      <input
                        id="password"
                        name="password"
                        type="password"
                        autoComplete="current-password"
                        required
                        className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                        value={data.password}
                        onChange={(e) => setData({ ...data, password: e.target.value })}
                      />
                    </div>
                  </div>
                  <div className="space-y-1">
                    <label htmlFor="billing_address" className="block text-sm font-medium text-gray-700">
                      Billing Address
                    </label>
                    <div className="mt-1">
                      <input
                        id="billing_address"
                        name="billing_address"
                        type="text"
                        autoComplete="billing_address"
                        required
                        className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                        value={data.billing_address}
                        onChange={(e) => setData({ ...data, billing_address: e.target.value })}
                      />
                    </div>
                  </div>
                  <div className="space-y-1">
                    <label htmlFor="shipping_address" className="block text-sm font-medium text-gray-700">
                      Shipping Address
                    </label>
                    <div className="mt-1">
                      <input
                        id="shipping_address"
                        name="shipping_address"
                        type="text"
                        autoComplete="shipping_address"
                        required
                        className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                        value={data.shipping_address}
                        onChange={(e) => setData({ ...data, shipping_address: e.target.value })}
                      />
                    </div>
                  </div>
                  <div className="space-y-1">
                    <label htmlFor="payment_methods" className="block text-sm font-medium text-gray-700">
                      Payment Methods
                    </label>
                    <div className="mt-1">
                      <input
                        id="payment_methods"
                        name="payment_methods"
                        type="text"
                        autoComplete="payment_methods"
                        required
                        className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                        value={data.payment_methods}
                        onChange={(e) => setData({ ...data, payment_methods: e.target.value })}
                      />
                    </div>
                  </div>
                  {/* Add Image Upload */}
                  <div className="space-y-1">
                    <label htmlFor="image" className="block text-sm font-medium text-gray-700">
                      Image
                    </label>
                    <div className="mt-1">
                      <input
                        id="image"
                        name="image"
                        type="file"
                        autoComplete="image"
                        required
                        className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                        onChange={handleImageUpload}
                      />
                    </div>
                  </div>
                    

                  <div className="flex items-center justify-between">
                    <div className="flex items-center">
                      <input
                        id="remember-me"
                        name="remember-me"
                        type="checkbox"
                        className="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
                      />
                      <label htmlFor="remember-me" className="ml-2 block text-sm text-gray-900">
                        Remember me
                      </label>
                    </div>

                    <div className="text-sm">
                      <a href="#" className="font-medium text-indigo-600 hover:text-indigo-500">
                        Forgot your password?
                      </a>
                    </div>
                  </div>

                  <div>
                    <button
                      type="submit"
                      className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                      onClick={handleSubmit}
                    >
                      Register
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
        <div className="hidden lg:block relative w-0 flex-1">
          <img
            className="absolute inset-0 h-full w-full object-cover"
            src="https://images.unsplash.com/photo-1505904267569-f02eaeb45a4c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1908&q=80"
            alt=""
          />
        </div>
      </div>
    </div>
  )
}
