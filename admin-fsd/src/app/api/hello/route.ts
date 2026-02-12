import {NextRequest, NextResponse} from 'next/server'

// GET /api/hello
export async function GET(request: NextRequest) {
  return NextResponse.json({
    message: 'Hello from Next.js API!',
    timestamp: new Date().toISOString(),
  })
}

// POST /api/hello
export async function POST(request: NextRequest) {
  const body = await request.json()

  return NextResponse.json({
    message: 'Data received',
    data: body,
  })
}
